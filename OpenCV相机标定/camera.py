import numpy as np

rmse = 0.15536906910078815
distortion_coefficients = np.array([[-0.29297163675166843, 0.10770696222739479, 0.0013103837668624015, -3.110188110977551e-05, 0.04347981038605618]], dtype=np.float32)
raw_camera_matrix = np.array([[534.0708836433579, 0.0, 341.53407552622144], [0.0, 534.119145952222, 232.9456525980155], [0.0, 0.0, 1.0]], dtype=np.float32)
undistort_camera_matrix = np.array([[519.0968582352713, 0.0, 320.0], [0.0, 519.1437673884751, 240.0], [0.0, 0.0, 1.0]], dtype=np.float32)
roi = 0, 0, 640, 480
image_size = 640, 480
print("distortion_coefficients")
print(distortion_coefficients)
print("raw_camera_matrix")
print(raw_camera_matrix)
print("undistort_camera_matrix")
print(undistort_camera_matrix)

