# import numpy as np
#
#
# def scale(value=None, matrix=None):
#     if matrix is None:
#         matrix = np.identity(4)
#
#     return np.matmul(np.diag(value + (1,)), matrix).transpose()
#
#
# def translation(value=None, matrix=None):
#     if matrix is None:
#         matrix = np.identity(4)
#
#     return np.matmul(np.array([
#         [1, 0, 0, value[0]],
#         [0, 1, 0, value[1]],
#         [0, 0, 1, value[2]],
#         [0, 0, 0, 1]
#     ], dtype=np.float32), matrix)
#
#
# def rotate(angle, value=None, matrix=None):
#     if matrix is None:
#         matrix = np.identity(4)
#
#     magnitude = np.sqrt(value[0] ** 2 + value[1] ** 2 + value[2] ** 2)
#
#     axis = (value[0] / magnitude, value[1] / magnitude, -value[2] / magnitude)
#
#     r_angle = np.radians(angle)
#
#     c_angle = 1 - np.cos(r_angle)
#
#     s_angle = np.sin(r_angle)
#
#     return np.matmul(np.array([
#         [1 - c_angle + axis[0] ** 2 * c_angle,
#          axis[0] * axis[1] * c_angle - axis[2] * s_angle,
#          axis[0] * axis[2] * c_angle + axis[1] * s_angle, 0],
#
#         [axis[1] * axis[0] * c_angle + axis[2] * s_angle,
#          1 - c_angle + axis[1] ** 2 * c_angle,
#          axis[1] * axis[2] * c_angle - axis[0] * s_angle, 0],
#
#         [axis[2] * axis[0] * c_angle - axis[1] * s_angle,
#          axis[2] * axis[1] * c_angle + axis[0] * s_angle,
#          1 - c_angle + axis[2] ** 2 * c_angle, 0],
#         [0, 0, 0, 1]
#     ], dtype=np.float32), matrix)
#
#
# if __name__ == "__main__":
#     sd = np.identity(4)
#     print(np.identity(4))
#
#     # print(scale((2, 2, 2), translation((1, 2, 3), rotate(30, (1, 0, 0)))))
#     # print(rotate(30, (1, 1.5, -1)))
#     print(translation((1, 2, 3)))
#
#     print(np.sin(np.radians(90)))
#
#     print(3 ** 3)
