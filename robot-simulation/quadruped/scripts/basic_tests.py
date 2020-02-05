from comm.pwm import PWM
from time import sleep

driver = PWM(0x40)
driver.setPWMFreq(50)

def map(z, x, y, a, b):
  # x to y is the old range
  # a to b is the new range
  # z is somewhere in between x and y
  # c is somewhere in between a and b
  c = (z - x) * (b - a) / (y - x) + a
  return c

class Joint:
  def __init__(self, ch, a, b, x, y, n):
    self.ch = ch

    # min and max pwm values
    self.n = n # value at neutral position (angle zero)
    self.a = a
    # the 'a' pwm signal corresponds to:
    #   hip: towards the sides and away from either the back or front
    #   knee: upper leg towards ground
    #   ankle: lower leg towards the upper leg from the perpendicular
    self.b = b
    # the 'b' pwm signal corresponds to:
    #   hip: away from the sides and towards either back or front
    #   knee: upper leg towards the sky
    #   ankle: lowerleg away from the upper leg from the perpendicular

    # min and max angle values in degrees
    # x is negative, corresponds to 'a'
    self.x = x
    # y is positive, corresponds to 'b'
    self.y = y

  def neutral_pose(self):
    driver.setPWM(self.ch, 0, self.n)

  def pose(self, z):
    c = map(z, self.x, self.y, self.a, self.b)
    driver.setPWM(self.ch, 0, c)

  def off(self):
    driver.setPWM(self.ch, 0, 0)

MIN_ANGLE = -70
MAX_ANGLE = 70


hip_front_left = Joint(0, 165, 500, MIN_ANGLE, MAX_ANGLE, 330)
hip_front_right = Joint(3, 510, 160, MIN_ANGLE, MAX_ANGLE, 330)
hip_back_left = Joint(6, 500, 155, MIN_ANGLE, MAX_ANGLE, 320)
hip_back_right = Joint(9, 170, 510, MIN_ANGLE, MAX_ANGLE, 350)

knee_front_left = Joint(1, 165, 505, MIN_ANGLE, MAX_ANGLE, 345)
knee_front_right = Joint(4, 465, 130, MIN_ANGLE, MAX_ANGLE, 280)
knee_back_left = Joint(7, 475, 120, MIN_ANGLE, MAX_ANGLE, 290)
knee_back_right = Joint(10, 140, 485, MIN_ANGLE, MAX_ANGLE, 315)

ankle_front_left = Joint(2, 400, 190, MIN_ANGLE, MAX_ANGLE, 350)
ankle_front_right = Joint(5, 220, 450, MIN_ANGLE, MAX_ANGLE, 280)
ankle_back_left = Joint(8, 250, 470, MIN_ANGLE, MAX_ANGLE, 290)
ankle_back_right = Joint(11, 380, 170, MIN_ANGLE, MAX_ANGLE, 335)

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

def quadruped_neutral_pose():
  for hip, knee, ankle in zip(hips, knees, ankles):
    hip.neutral_pose()
    knee.neutral_pose()
    ankle.neutral_pose()

def turn_off_everything():
  for hip, knee, ankle in zip(hips, knees, ankles):
    hip.off()
    knee.off()
    ankle.off()

t = 0.25
s = 2.0

print 'Quadruped positioning to: neutral pose'
quadruped_neutral_pose()
sleep(s)
print 'DONE \n'
print 'turn off all the joints for a few seconds'
turn_off_everything()
sleep(s)
print 'DONE \n'

print 'TEST ZERO'
for hip, knee, ankle in zip(hips, knees, ankles):
  hip.pose(0)
  sleep(t)
  knee.pose(0)
  sleep(t)
  ankle.pose(0)
  sleep(t)

sleep(s)
print 'DONE \n'

#========================================
print 'TEST ONE: hip angles are zero'
for hip in hips:
  hip.pose(0)
  sleep(t)

sleep(s)
print 'DONE \n'

#========================================
print 'TEST TWO: hip angles are positive'
for hip in hips:
  hip.pose(30)
  sleep(t)

sleep(s)
print 'DONE \n'

#========================================
print 'TEST THREE: hip angles are negative'
for hip in hips:
  hip.pose(-60)
  sleep(t)

sleep(s)
print 'DONE \n'

#========================================
print 'Quadruped positioning to: neutral pose'
quadruped_neutral_pose()
sleep(s)
print 'DONE \n'

#========================================
print 'TEST FOUR: knee angles are zero'
for knee in knees:
  knee.pose(0)
  sleep(t)

sleep(s)
print 'DONE \n'

#========================================
print 'TEST FIVE: knee angles are positive'
for knee in knees:
  knee.pose(60)
  sleep(t)

sleep(s)
print 'DONE \n'

#========================================
print 'TEST SIX: knee angles are negative'
for knee in knees:
  knee.pose(-60)
  sleep(t)

sleep(s)
print 'DONE \n'

#========================================
print 'Quadruped positioning to: neutral pose'
quadruped_neutral_pose()
sleep(s)
print 'DONE \n'

#========================================
print 'TEST SEVEN: ankle angles are zero'
for ankle in ankles:
  ankle.pose(0)
  sleep(t)

sleep(s)
print 'DONE \n'

#========================================
print 'TEST EIGHT: ankle angles are negative'
for ankle in ankles:
  ankle.pose(-60)
  sleep(t)

sleep(s)
print 'DONE \n'

#========================================
print 'TEST NINE: ankle angles are positive'
for ankle in ankles:
  ankle.pose(60)
  sleep(t)

sleep(s)
print 'DONE \n'
