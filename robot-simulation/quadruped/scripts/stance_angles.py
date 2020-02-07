import numpy as np

# Resting stance

# w - foot position away from hip servo / body at resting/neutral stance
# h - height form the floor
# A - upper leg length
# B - lower leg length
# theta = theta1 = theta2
# theta1 = angle of upper leg wrt to the horizontal
# theta2 = angle of the lower leg wrt to line perpendicular to the upper leg

def find_resting_stance_foot_position(theta, A=86, B=128):
  angle = np.radians(theta)
  w = A*np.cos(angle)
  h = B - A*np.sin(angle)
  return w, h

# propelling forward
# y - foot position from hip servo / body at sidestep stance
# v - foot position from hip servo / body at reaching stance
# beta - reach hip angle (theta in figure) (hip angle at reaching stance)
# alpha - sidestep hip angle (hip angle at side step stance)
# w - foot position away from the body at neutral/resting stance

def find_propel_forward_values(alpha, w):
  k = w*np.cos(np.radians(45)) # cos(45) == sin(45)
  alpha = np.radians(alpha)
  y = k / np.cos(alpha)
  c = k*np.tan(alpha) #  y * np.sin(alpha)
  m = (2*k + c) / k
  beta = np.arctan(m)
  v = k / np.cos(beta)
  return np.degrees(beta), v, y

# side step stance or reaching stance
# A - upper leg length
# B - lower leg length
# w - foot position away from hip servo / body at stance (reaching or sidestep stance)
# h - height form the floor
# theta1 = angle of upper leg wrt to the horizontal
# theta2 = angle of the lower leg wrt to line perpendicular to the upper leg
def find_stance_angles(w, h, A=86, B=128):
  C = np.sqrt(h**2 + w**2)
  x = np.arcsin(w / C)

  cos_gamma = (A**2 + B**2 - C**2) / (2*A*B)
  gamma = np.arccos(cos_gamma)
  cos_y = (A**2 + C**2 - B**2) / (2*A*C)

  y = np.arccos(cos_y)

  theta1 = x + y - np.radians(90)
  theta2 = np.radians(90) - gamma
  return np.degrees(theta1), np.degrees(theta2)

# A - upper leg length
# B - lower leg length
A = 86
B = 128

# theta1 = angle of upper leg wrt to the horizontal
# theta2 = angle of the lower leg wrt to line perpendicular to the upper leg

# beta - hip angle at reaching stance
# alpha - hip angle at side step stance

# theta = theta1 = theta2 angles at resting stance
THETA = 40 # Between 30 and 50
ALPHA = 5 # Between 0 and 20

w_resting, h = find_resting_stance_foot_position(THETA, A, B)
# w_resting - foot position away from hip servo / body at resting stance
# h - height from the floor (at resting stance)


# y_side_step - foot position from hip servo / body at sidestep stance
# v - foot position from hip servo / body at reaching stance
# beta - hip angle at reaching stance
BETA, v_reach, y_sidestep = find_propel_forward_values(ALPHA, w_resting)

theta1_sidestep, theta2_sidestep = find_stance_angles(y_sidestep, h, A, B)
theta1_reach, theta2_reach = find_stance_angles(v_reach, h, A, B)

print('Upper leg length in mm: ', A)
print('Lower leg length in mm: ', B)
print('Height from floor in mm: ', h)

print('-')
print("RESTING STANCE")
print("hip angle parallel to (shoulder) horizontal in degrees: 45")
print('knee angle parallel to (shoulder) horizonal in degrees: ', THETA)
print('ankle angle perpendicular to lowerleg in degrees: ', THETA)
print('foot position from hip in mm: ', w_resting)

print('-')
print("SIDESTEP STANCE")
print("hip angle parallel to (shoulder) horizontal in degrees:", ALPHA)
print('knee angle parallel to (shoulder) horizonal in degrees:', theta1_sidestep)
print('ankle angle perpendicular to lowerleg in degrees:', theta2_sidestep)
print('foot position from hip in mm: ', y_sidestep)

print('-')
print("REACHING STANCE")
print("hip angle parallel to (shoulder) horizontal in degrees:", BETA)
print('knee angle parallel to (shoulder) horizonal in degrees:', theta1_reach)
print('ankle angle perpendicular to lowerleg in degrees:', theta2_reach)
print('foot position from hip in mm: ', v_reach)

#neutral hip angle is 45
NEUTRAL = 45
hip_angle_resting = 0
hip_angle_sidestep = ALPHA + NEUTRAL
hip_angle_reach = BETA - NEUTRAL

print('-')
print("Absolute hip angles based on servo orientation (degrees):")
print("resting: ", hip_angle_resting)
print("side_step: ", hip_angle_sidestep)
print("reaching: ", hip_angle_reach)

# Upper leg length in mm:  86
# Lower leg length in mm:  128
# Height from floor in mm:  72.72026556695762
# -
# RESTING STANCE
# hip angle parallel to (shoulder) horizontal in degrees: 45
# knee angle parallel to (shoulder) horizonal in degrees:  40
# ankle angle perpendicular to lowerleg in degrees:  40
# foot position from hip in mm:  65.8798221082321
# -
# SIDESTEP STANCE
# hip angle parallel to (shoulder) horizontal in degrees: 5
# knee angle parallel to (shoulder) horizonal in degrees: 38.58250661168782
# ankle angle perpendicular to lowerleg in degrees: 47.7826582117061
# foot position from hip in mm:  46.76201253161473
# -
# REACHING STANCE
# hip angle parallel to (shoulder) horizontal in degrees: 64.40350450294298
# knee angle parallel to (shoulder) horizonal in degrees: 35.24987500744083
# ankle angle perpendicular to lowerleg in degrees: 18.169817718893693
# foot position from hip in mm:  107.82585845793648
# -
# Absolute hip angles based on servo orientation:
# resting:  0
# side_step:  50
# reaching:  19.40350450294298



