from comm.pwm import PWM
from time import sleep

# CALIBRATION
CHANNEL = 0 # Channel of the servo joint
VALUE = 0 # Value to accomplish the pose
DELAY = 0.5

driver = PWM(0x40)
driver.setPWMFreq(50)

while True:
  driver.setPWM(CHANNEL, 0, VALUE)
  sleep(DELAY)
