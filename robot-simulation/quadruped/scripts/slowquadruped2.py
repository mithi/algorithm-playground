#----------------------------
# WALK ALGORITHM CONSTANTS FOR CALIBRATION
#----------------------------
TEST = True

INCREMENTS = 20
WALK_STEPS = 5
DELAY = 0.5

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
FRONT_LEFT = 'front left'
FRONT_RIGHT = 'front right'
BACK_LEFT = 'back left'
BACK_RIGHT = 'back right'

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
  def __init__(self, channel, pwm_min, pwm_max, angle_min, angle_max):
    self.channel = channel

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
    self.pose(0)

  def pose(self, angle):
    pwm_value = map(angle, self.angle_min, self.angle_max, self.pwm_min, self.pwm_max)
    print 'POSE ch: ', self.channel, 'angle: ', angle, 'pwm:', int(pwm_value)
    if TEST == False:
      driver.setPWM(self.ch, 0, int(pwm_value))
    self.current_angle = angle

  def get_movement_increment(self, target_angle, increments):
    return (target_angle - self.current_angle) / increments

  def move_by(self, da):
    self.pose(self.current_angle + da)

  def off(self):
    if TEST == False:
      driver.setPWM(self.ch, 0, 0)

#----------------------------
# QUADRUPED CORE STANCES
#----------------------------
class QuadrupedCore:


  def __init__(self, legs):
    self.legs = legs
    self.zero_pose()

  def off(self):
    for joints in self.legs.values():
      for joint in joints.values():
        joint.off()

  def zero_pose(self, delay=0):
    for joints in self.legs.values():
      for joint in joints.values():
        joint.pose(0)

  def pose(self, position, hip_angle, knee_angle, ankle_angle, delay):
    self.legs[position]['hip'].pose(hip_angle)
    self.legs[position]['knee'].pose(knee_angle)
    self.legs[position]['ankle'].pose(ankle_angle)
    sleep(delay)

  def slow_pose(self, position, hip_angle, knee_angle, ankle_angle, delay):

    hip = self.legs[position]['hip']
    knee = self.legs[position]['knee']
    ankle = self.legs[position]['ankle']

    dh = hip.get_movement_increment(hip_angle, INCREMENTS)
    dk = knee.get_movement_increment(knee_angle, INCREMENTS)
    da = ankle.get_movement_increment(ankle_angle, INCREMENTS)

    dt = delay / INCREMENTS

    for i in xrange(INCREMENTS):
      print 'slow pose: # ', i
      hip.move_by(dh)
      knee.move_by(dk)
      ankle.move_by(da)
      sleep(dt)

  def bend_up(self, position, delay=0):

    knee = self.legs[position]['knee']
    ankle = self.legs[position]['ankle']

    dk = knee.get_movement_increment(KNEE_BENTUP, INCREMENTS)
    da = ankle.get_movement_increment(ANKLE_BENTUP, INCREMENTS)
    dt = delay / INCREMENTS

    for i in xrange(INCREMENTS):
      print 'bend up: # ', i
      knee.move_by(dk)
      ankle.move_by(da)
      sleep(dt)

  def move_joints_simultaneously(self, hip_angle, knee_angle, ankle_angle, delay):
    dt = delay / INCREMENTS
    d_angles = {}

    for position, joints in self.legs.items():
      dh = joints['hip'].get_movement_increment(hip_angle, INCREMENTS)
      dk = joints['knee'].get_movement_increment(knee_angle, INCREMENTS)
      da = joints['ankle'].get_movement_increment(ankle_angle, INCREMENTS)

      d_angles[position] = {
        'hip': dh,
        'knee': dk,
        'ankle': da
      }

    for i in xrange(INCREMENTS):
      print 'move joints simultaneously: # ', i
      for position, joints in self.legs.items():

        dh = d_angles[position]['hip']
        dk = d_angles[position]['knee']
        da = d_angles[position]['ankle']

        joints['hip'].move_by(dh)
        joints['knee'].move_by(dk)
        joints['ankle'].move_by(da)

        sleep(dt)

  def rest(self, position, delay=0):
    self.slow_pose(position, HIP_REST, KNEE_REST, ANKLE_REST, delay)

  def side_step(self, position, delay=0):
    self.slow_pose(position, HIP_SIDESTEP, KNEE_SIDESTEP, ANKLE_SIDESTEP, delay)

  def reach(self, position, delay=0):
    self.slow_pose(position, HIP_REACH, KNEE_REACH, ANKLE_REACH, delay)

  def high_pose_simultaneously(self, delay):
    self.move_joints_simultaneously(0, -90, 90, delay)

  def rest_pose_simultaneously(self, delay):
    self.move_joints_simultaneously(HIP_REST, KNEE_REST, ANKLE_REST, delay)

#----------------------------
# QUADRUPED JOINT SETUP
#----------------------------
ANGLE_MIN = -70
ANGLE_MAX = 70

hip_front_left = Joint(channel=0, pwm_min=165, pwm_max=500, angle_min=ANGLE_MIN, angle_max=ANGLE_MAX)
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

LEGS = {
  'front left': {
    'hip': hip_front_left,
    'knee': knee_front_left,
    'ankle': ankle_front_left
  },

  'front right': {
    'hip': hip_front_right,
    'knee': knee_front_right,
    'ankle': ankle_front_right
  },

  'back left': {
    'hip': hip_back_left,
    'knee': knee_back_left,
    'ankle': ankle_back_left
  },

  'back right': {
    'hip': hip_back_right,
    'knee': knee_back_right,
    'ankle': ankle_back_right
  }
}


#----------------------------
# INSTANTIATE QUADRUPED
#----------------------------
robot = QuadrupedCore(LEGS)

#----------------------------
# WALK TEST
#----------------------------
robot.zero_pose(DELAY)
robot.rest_pose_simultaneously(DELAY)

# STEP ZERO
# Go to starting position
# from neutral (all 0 degrees)
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

robot.rest_pose_simultaneously(DELAY)
robot.high_pose_simultaneously(DELAY)
robot.off()

