import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

class Point:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def get_point_wrt(self, reference_frame):
    # given frame_ab which is the pose of frame_b wrt frame_a
    # given a point as defined wrt to frame_b
    # return point defined wrt to frame a
    p = np.array([self.x, self.y, self.z, 1])
    p = np.matmul(reference_frame, p)
    return Point(p[0], p[1], p[2])

# rotate about y, translate in x
def frame_yrotate_xtranslate(theta, x):
  theta = np.radians(theta)
  cos_theta = np.cos(theta)
  sin_theta = np.sin(theta)

  return np.array([
    [cos_theta, 0, sin_theta, x],
    [0, 1, 0, 0],
    [-sin_theta, 0, cos_theta, 0],
    [0, 0, 0, 1]
  ])

# rotate about z, translate in x and y
def frame_zrotate_xytranslate(theta, x, y):
  theta = np.radians(theta)
  cos_theta = np.cos(theta)
  sin_theta = np.sin(theta)

  return np.array([
    [cos_theta, -sin_theta, 0, x],
    [sin_theta, cos_theta, 0, y],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
  ])

# -------------
# LINKAGE
# -------------
# Neutral position of the linkages (alpha=0, beta=0, gamma=0)
# note that at neutral position:
#  link b and link c are perpendicular to each other
#  link a and link b form a straight line
#  link a and coincide with  x axis
#
# alpha - the able linkage a makes with x_axis about z axis
# beta - the angle that linkage a makes with linkage b
# gamma - the angle that linkage c make with the line perpendicular to linkage b
#
#
# MEASUREMENTS
#
#  |--- a--------|--b--|
#  |=============|=====| p2 -------
#  p0            p1    |          |
#                      |          |
#                      |          c
#                      |          |
#                      |          |
#                      | p3  ------
#
#  z axis
#  |
#  |
#  |------- x axis
# origin
#
#
# ANGLES beta and gamma
#                /
#               / beta
#         ---- /* ---------
#        /    //\\        \
#       b    //  \\        \
#      /    //    \\        c
#     /    //beta  \\        \
# *=======* ---->   \\        \
# |---a---|          \\        \
#                     *-----------
#
# |--a--|---b----|
# *=====*=========* -------------
#               | \\            \
#               |  \\            \
#               |   \\            c
#               |    \\            \
#               |gamma\\            \
#               |      *----------------
#
class Linkage:
  COLOR_A = '#c0392b'
  COLOR_B = '#e67e22'
  COLOR_C = '#e74c3c'
  LINE_SIZE = 5
  def __init__(self, a, b, c, alpha=0, beta=0, gamma=0, new_x_axis=0, new_origin=Point(0, 0, 0)):
    self.store_linkage_attributes(a, b, c, new_x_axis, new_origin)
    self.save_new_pose(alpha, beta, gamma)

  def store_linkage_attributes(self, a, b, c, new_x_axis, new_origin):
    self._a = a
    self._b = b
    self._c = c
    self._new_origin = new_origin
    self._new_x_axis = new_x_axis

  def save_new_pose(self, alpha, beta, gamma):
    self._alpha = alpha
    self._beta = beta
    self._gamma = gamma

    # frame_ab is the pose of frame_b wrt frame_a
    frame_01 = frame_yrotate_xtranslate(theta=-self._beta, x=self._a)
    frame_12 = frame_yrotate_xtranslate(theta=90-self._gamma, x=self._b)
    frame_23 = frame_yrotate_xtranslate(theta=0, x=self._c)

    frame_02 = np.matmul(frame_01, frame_12)
    frame_03 = np.matmul(frame_02, frame_23)
    new_frame = frame_zrotate_xytranslate(self._new_x_axis + self._alpha, self._new_origin.x, self._new_origin.y)

    # find points wrt to body contact point
    p0 = Point(0, 0, 0)
    p1 = p0.get_point_wrt(frame_01)
    p2 = p0.get_point_wrt(frame_02)
    p3 = p0.get_point_wrt(frame_03)

    # find points wrt to center of gravity
    self.p0 = self._new_origin
    self.p1 = p1.get_point_wrt(new_frame)
    self.p2 = p2.get_point_wrt(new_frame)
    self.p3 = p3.get_point_wrt(new_frame)

  def change_pose(self, alpha=None, beta=None, gamma=None):
    if alpha is None:
      alpha = self._alpha
    if beta is None:
      beta = self._beta
    if gamma is None:
      gamma = self._gamma
    self.save_new_pose(alpha, beta, gamma)

  def draw(self):
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5)
    ax = plt.axes(projection='3d')
    ax.set_zlim3d(-150, 150)
    ax.set_ylim3d(-100, 100)
    ax.set_xlim3d(-100, 100)

    leg = self

    # from body contact to hip joint
    ax.plot3D(
      [leg.p0.x, leg.p1.x],
      [leg.p0.y, leg.p1.y],
      [leg.p0.z, leg.p1.z],
      color=Linkage.COLOR_A,
      linewidth=Linkage.LINE_SIZE
    )
    # hip joint to knee joint
    ax.plot3D(
      [leg.p1.x, leg.p2.x],
      [leg.p1.y, leg.p2.y],
      [leg.p1.z, leg.p2.z],
      color=Linkage.COLOR_B,
      linewidth=Linkage.LINE_SIZE
    )
    # from knee joint to ankle joints
    ax.plot3D(
      [leg.p2.x, leg.p3.x],
      [leg.p2.y, leg.p3.y],
      [leg.p2.z, leg.p3.z],
      color=Linkage.COLOR_C,
      linewidth=Linkage.LINE_SIZE
    )
  plt.show()

# -------------
# HEXAGON
# -------------
#
#
#               head
#     point2 *---*---* point1
#           /    |    \
#          /     |     \
#  point3 *-----cog-----* point0
#          \     |     /
#           \    |    /
#     point4 *---*---* point5
#
#
# MEASUREMENTS f, s, and m
#
#       |-f-|
#       *---*---*--------
#      /    |    \     |
#     /     |     \    s
#    /      |      \   |
#   *------cog------* ---
#    \      |      /|
#     \     |     / |
#      \    |    /  |
#       *---*---*   |
#           |       |
#           |---m---|
#
#    y axis
#    ^
#    |
#    |
#    ----> x axis
#  cog (origin)
#
#
# Relative x-axis, for each attached linkage
#
#        x2         x1
#         \         /
#          *---*---*
#         /    |    \
#        /     |     \
#       /      |      \
#  x3--*------cog------*--x0
#       \      |      /
#        \     |     /
#         \    |    /
#          *---*---*
#         /        \
#        x4        x5
#
class Hexagon:
  LINE_COLOR = '#9b59b6'
  LINE_SIZE = 5
  POINT_COLOR = '#9b59b6'
  COG_COLOR = '#2ecc71'
  POINT_SIZE = 10
  HEAD_SIZE = 15
  COG_SIZE = 15

  def __init__(self, f, m, s):
    self.f = f
    self.m = m
    self.s = s

    self.cog = Point(0, 0, 0)
    self.head = Point(0, m, 0)
    self.points = [
      Point(m, 0, 0),
      Point(f, s, 0),
      Point(-f, s, 0),
      Point(-m, 0, 0),
      Point(-f, -s, 0),
      Point(f, -s, 0),
    ]

    self.new_x_axes = [
      0, 45, 135, 180, 225, 315
    ]

class VirtualHexapod:
  def __init__(self, a=0, b=0, c=0, f=0, m=0, s=0):
    self.linkage_measurements = [a, b, c]
    self.body_measurements = [f, m, s]
    self.origin_hexagon = Hexagon(f, m, s)
    self.store_neutral_legs(a, b, c)

  def store_neutral_legs(self, a, b, c):
    self.legs = []
    for point, theta in zip(self.origin_hexagon.points, self.origin_hexagon.new_x_axes):
      linkage = Linkage(a, b, c, new_x_axis=theta, new_origin=point)
      self.legs.append(linkage)

  def draw_top_view(self):
    plt.xlim(-150, 150)
    plt.ylim(-150, 150)

    hexagon = self.origin_hexagon

    hx = [point.x for point in hexagon.points]
    hy = [point.y for point in hexagon.points]
    hx.append(hx[0])
    hy.append(hy[0])

    plt.plot(
      hx,
      hy,
      color=Hexagon.LINE_COLOR,
      linewidth=Hexagon.LINE_SIZE,
      markersize=Hexagon.POINT_SIZE,
      marker='o'
    )

    # draw center of gravity
    plt.plot(
      [hexagon.cog.x],
      [hexagon.cog.y],
      marker='o',
      color=Hexagon.COG_COLOR,
      markersize=Hexagon.COG_SIZE
    )

    # draw head
    plt.plot(
      [hexagon.head.x],
      [hexagon.head.y],
      marker='o',
      linewidth=0,
      color=Hexagon.POINT_COLOR,
      markersize=Hexagon.HEAD_SIZE
    )
    # ------------------
    # draw legs (LINKAGES)
    # ------------------
    for leg in self.legs:

      # from body contact to hip joint
      plt.plot(
        [leg.p0.x, leg.p1.x],
        [leg.p0.y, leg.p1.y],
        color=Linkage.COLOR_A,
        linewidth=Linkage.LINE_SIZE
      )

      # hip joint to knee joint
      plt.plot(
        [leg.p1.x, leg.p2.x],
        [leg.p1.y, leg.p2.y],
        color=Linkage.COLOR_B,
        linewidth=Linkage.LINE_SIZE
      )

      # from knee joint to ankle joints
      plt.plot(
        [leg.p2.x, leg.p3.x],
        [leg.p2.y, leg.p3.y],
        color=Linkage.COLOR_C,
        linewidth=Linkage.LINE_SIZE
      )
    plt.show()

  def draw(self):
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5)
    ax = plt.axes(projection='3d')
    ax.set_zlim3d(-150, 150)
    ax.set_ylim3d(-100, 100)
    ax.set_xlim3d(-100, 100)

    # ------------------
    # draw body HEXAGON
    # ------------------
    hexagon = self.origin_hexagon

    # color the face of the polygon
    hx = [point.x for point in hexagon.points]
    hy = [point.y for point in hexagon.points]
    hz = [point.z for point in hexagon.points]

    vertices = [list(zip(hx, hy, hz))]
    collection = Poly3DCollection(
      vertices,
      facecolors=Hexagon.LINE_COLOR,
      alpha=0.5)

    ax.add_collection3d(collection)

    # draw the edges and vertices
    # append the initial point to connect
    # the last point to the first point
    hx.append(hx[0])
    hy.append(hy[0])
    hz.append(hz[0])

    ax.plot3D(
      hx,
      hy,
      hz,
      color=Hexagon.LINE_COLOR,
      linewidth=Hexagon.LINE_SIZE,
      markersize=Hexagon.POINT_SIZE,
      marker='o'
    )

    # draw center of gravity
    ax.plot3D(
      [hexagon.cog.x],
      [hexagon.cog.y],
      [hexagon.cog.z],
      marker='o',
      color=Hexagon.COG_COLOR,
      markersize=Hexagon.COG_SIZE
    )

    # draw head
    ax.plot3D(
      [hexagon.head.x],
      [hexagon.head.y],
      [hexagon.head.z],
      marker='o',
      linewidth=0,
      color=Hexagon.POINT_COLOR,
      markersize=Hexagon.HEAD_SIZE
    )

    # ------------------
    # draw legs (LINKAGES)
    # ------------------
    for leg in self.legs:

      # from body contact to hip joint
      ax.plot3D(
        [leg.p0.x, leg.p1.x],
        [leg.p0.y, leg.p1.y],
        [leg.p0.z, leg.p1.z],
        color=Linkage.COLOR_A,
        linewidth=Linkage.LINE_SIZE
      )

      # hip joint to knee joint
      ax.plot3D(
        [leg.p1.x, leg.p2.x],
        [leg.p1.y, leg.p2.y],
        [leg.p1.z, leg.p2.z],
        color=Linkage.COLOR_B,
        linewidth=Linkage.LINE_SIZE
      )

      # from knee joint to ankle joints
      ax.plot3D(
        [leg.p2.x, leg.p3.x],
        [leg.p2.y, leg.p3.y],
        [leg.p2.z, leg.p3.z],
        color=Linkage.COLOR_C,
        linewidth=Linkage.LINE_SIZE
      )
    plt.show()

FRONT_LENGTH = 20
SIDE_LENGTH= 30
MID_LENGTH = 40
HIP_LENGTH =10
KNEE_LENGTH = 40
ANKLE_LENGTH = 60

virtual_hexapod = VirtualHexapod(HIP_LENGTH, KNEE_LENGTH, ANKLE_LENGTH, FRONT_LENGTH, MID_LENGTH, SIDE_LENGTH)
virtual_hexapod.draw()
virtual_hexapod.draw_top_view()
