#----------------------------
# WALK ALGORITHM CONSTANTS FOR CALIBRATION
#----------------------------
TEST = False

WALK_STEPS = 1
DELAY = 1.0

KNEE_BENTUP = 10
ANKLE_BENTUP = -10

HIP_SIDESTEP = -60
KNEE_SIDESTEP = -30
ANKLE_SIDESTEP = 30

HIP_REACH = 10
KNEE_REACH = -15
ANKLE_REACH = 20

HIP_REST = -10
KNEE_REST = -30
ANKLE_REST = 30

#----------------------------
# PACKAGES, HELPERS, DRIVER SETUP
#----------------------------
from time import sleep

if TEST == False:
  from comm.pwm import PWM
  driver = PWM(0x40)
  driver.setPWMFreq(50)

# Note: These should be enums
FRONT_LEFT = 0
FRONT_RIGHT = 1
BACK_LEFT = 2
BACK_RIGHT = 3

if TEST == True:
  DELAY = 0.0

def map(z, x, y, a, b):
  # x to y is the old range
  # a to b is the new range
  # z is somewhere in between x and y
  # c is somewhere in between a and b
  c = (z - x) * (b - a) / (y - x) + a
  return c

#----------------------------
# QUADRUPED JOINT
#----------------------------
class Joint:
  def __init__(self, ch, pwm_min, pwm_max, angle_min, angle_max):
    self.ch = ch

    # min,and max pwm values
    self.pwm_min = pwm_min
    # the 'min_pwm' pwm signal corresponds to:
    #   hip: towards the sides and away from either the back or front
    #   knee: upper leg towards ground
    #   ankle: lower leg towards the upper leg from the perpendicular
    self.pwm_max = pwm_max
    # the 'pwm_max' pwm signal corresponds to:
    #   hip: away from the sides and towards either back or front
    #   knee: upper leg towards the sky
    #   ankle: lowerleg away from the upper leg from the perpendicular

    # min,and max values in degrees
    # angle_min is negative, corresponds to 'pwm_min'
    self.angle_min = angle_min
    # angle_max is positive, corresponds to 'pwm_max'
    self.angle_max = angle_max

  def pose(self, angle):
    v = map(angle, self.angle_min, self.angle_max, self.pwm_min, self.pwm_max)
    print 'POSE ch: ', self.ch, 'angle: ', angle, 'pwm:', int(v)
    if TEST == False:
      driver.setPWM(self.ch, 0, int(v))

  def off(self):
    if TEST == False:
      driver.setPWM(self.ch, 0, 0)

#----------------------------
# QUADRUPED CORE STANCES
#----------------------------
class QuadrupedCore:
  def __init__(self, hips, knees, ankles):
    self.hips = hips
    self.knees = knees
    self.ankles = ankles
    self.joints = []
    for x, y, z in zip(hips, knees, ankles):
      self.joints.append(x)
      self.joints.append(y)
      self.joints.append(z)

  def off(self):
    for joint in self.joints:
      joint.off()

  def zero_pose(self, delay=0):
    for joint in self.joints:
      joint.pose(0)
    sleep(delay)

  def neutral_pose(self, delay=0):
    for position in [FRONT_LEFT, FRONT_RIGHT, BACK_LEFT, BACK_RIGHT]:
      self.rest(position)
    sleep(delay)

  def bend_up(self, position, delay=0):
    self.knees[position].pose(KNEE_BENTUP)
    self.ankles[position].pose(ANKLE_BENTUP)
    sleep(delay)

  def rest(self, position, delay=0):
    self.pose(position, HIP_REST, KNEE_REST, ANKLE_REST, delay)

  def side_step(self, position, delay=0):
    self.pose(position, HIP_SIDESTEP, KNEE_SIDESTEP, ANKLE_SIDESTEP, delay)

  def reach(self, position, delay=0):
    self.pose(position, HIP_REACH, KNEE_REACH, ANKLE_REACH, delay)

  def pose(self, position, hip_angle, knee_angle, ankle_angle, delay):
    self.hips[position].pose(hip_angle)
    self.knees[position].pose(knee_angle)
    self.ankles[position].pose(ankle_angle)
    sleep(delay)

#----------------------------
# QUADRUPED JOINT SETUP
#----------------------------
ANGLE_MIN = -70
ANGLE_MAX = 70

hip_front_left = Joint(0, 165, 500, ANGLE_MIN, ANGLE_MAX)
hip_front_right = Joint(3, 510, 160, ANGLE_MIN, ANGLE_MAX)
hip_back_left = Joint(6, 500, 155, ANGLE_MIN, ANGLE_MAX)
hip_back_right = Joint(9, 170, 510, ANGLE_MIN, ANGLE_MAX)
knee_front_left = Joint(1, 165, 505, ANGLE_MIN, ANGLE_MAX)
knee_front_right = Joint(4, 465, 130, ANGLE_MIN, ANGLE_MAX)
knee_back_left = Joint(7, 475, 120, ANGLE_MIN, ANGLE_MAX)
knee_back_right = Joint(10, 140, 485, ANGLE_MIN, ANGLE_MAX)
ankle_front_left = Joint(2, 400, 190, ANGLE_MIN, ANGLE_MAX)
ankle_front_right = Joint(5, 220, 450, ANGLE_MIN, ANGLE_MAX)
ankle_back_left = Joint(8, 250, 470, ANGLE_MIN, ANGLE_MAX)
ankle_back_right = Joint(11, 380, 170, ANGLE_MIN, ANGLE_MAX)

#----------------------------
# JOINT GROUPING
#----------------------------

# IMPORTANT! THE ORDER SHOULD BE FOLLOWED:
# [FRONT_LEFT, FRONT_RIGHT, BACK_LEFT, BACK_RIGHT]

hips = [
  hip_front_left,
  hip_front_right,
  hip_back_left,
  hip_back_right
]

knees = [
  knee_front_left,
  knee_front_right,
  knee_back_left,
  knee_back_right
]

ankles = [
  ankle_front_left,
  ankle_front_right,
  ankle_back_left,
  ankle_back_right
]

#----------------------------
# INSTANTIATE QUADRUPED
#----------------------------
robot = QuadrupedCore(hips, knees, ankles)

#----------------------------
# WALK TEST
#----------------------------
robot.zero_pose(DELAY)
robot.neutral_pose(DELAY)

# STEP ZERO
# Go to starting position
# from neutral (all  0 degrees)
# side step backward of front right leg
robot.bend_up(FRONT_RIGHT, DELAY)
robot.side_step(FRONT_RIGHT, DELAY)

for _ in xrange(WALK_STEPS):
  print 'STEP ONE'
  # from starting position
  # side step forward of back right leg
  robot.bend_up(BACK_RIGHT, DELAY)
  robot.side_step(BACK_RIGHT, DELAY)

  print 'STEP TWO'
  # reach forward of front right leg
  robot.bend_up(FRONT_RIGHT, DELAY)
  robot.reach(FRONT_RIGHT, DELAY)

  print 'STEP THREE'
  # propel the body forward by moving all four legs backward
  robot.side_step(FRONT_LEFT)
  robot.rest(FRONT_RIGHT)
  robot.reach(BACK_LEFT)
  robot.rest(BACK_RIGHT)
  sleep(DELAY)

  print 'STEP FOUR'
  # side step forward of left back leg
  robot.bend_up(BACK_LEFT, DELAY)
  robot.side_step(BACK_LEFT, DELAY)

  print 'STEP FIVE'
  # reach forward of left front leg
  robot.bend_up(FRONT_LEFT, DELAY)
  robot.reach(FRONT_LEFT, DELAY)

  print 'STEP SIX'
  # propel the body forward by moving all four legs backward
  robot.rest(FRONT_LEFT)
  robot.side_step(FRONT_RIGHT)
  robot.rest(BACK_LEFT)
  robot.reach(BACK_RIGHT)
  sleep(DELAY)
