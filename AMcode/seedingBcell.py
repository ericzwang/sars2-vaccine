# Seeding B cells dictionary
import csv
import numpy as np

seed1 = [0.076, 0.414, -0.135, 0.482, 0.168, 0.71, 0.19, 0.496, 0.818, 0.816,
         -0.155, 0.187, 0.621, 0.282, 0.176, 0.195, 0.236, -0.165, 0.509, -0.088,
         0.718, -0.074, 0.281, -0.135, 0.452, 0.092, 0.269, 0.647, 0.581, -0.067,
         0.625, 0.891, 0.586, 0.805, 0.02, 0.109, 0.397, -0.163, 0.344, -0.054,
         0.268, 0.332, 0.182, 0.375, 0.429, 0.107, 0.451, 0.263, 0.124, -0.035]
seed2 = [0.068, -0.062, 0.739, 0.222, -0.055, 0.149, 0.267, 0.574, 0.278, 0.683,
         0.367, 0.305, -0.098, -0.114, 0.282, 0.349, 0.508, 0.106, 0.638, -0.1,
         0.383, 0.21, 0.354, 0.819, -0.021, 0.476, 0.258, 0.696, 0.479, 0.091,
         0.598, 0.565, 0.106, 0.066, 0.023, 0.132, 0.24, -0.005, 0.433, 0.203,
         -0.057, 0.16, 0.617, 0.671, 0.623, 0.407, 0.316, -0.093, 0.27, 0.075]
seed3 = [0.016, 0.672, -0.122, 0.367, 0.284, 0.274, 0.535, 0.409, 0.809, -0.096,
         0.09, 0.499, 0.564, 0.603, 0.722, 0.333, 0.417, -0.028, 0.013, -0.169,
         0.03, -0.109, -0.067, 0.779, 0.754, 0.41, 0.231, -0.11, 0.054, 0.725,
         0.848, 0.26, 0.186, 0.529, 0.89, 0.302, 0.416, -0.13, 0.335, 0.139,
         0.228, 0.82, 0.034, 0.385, -0.167, 0.309, 0.474, -0.122, 0.154, -0.115]
seed4 = [-0.068, 0.474, 0.14, 0.562, 0.02, 0.377, 0.183, 0.534, 0.217, -0.173,
         0.659, 0.13, 0.082, 0.679, 0.672, 0.261, 0.772, 0.254, 0.579, 0.088,
         0.395, 0.442, 0.671, 0.235, 0.31, 0.448, -0.06, 0.238, 0.287, 0.726,
         0.15, 0.178, 0.083, 0.399, -0.009, 0.505, 0.352, 0.178, 0.506, -0.116,
         0.039, -0.154, 0.821, 0.039, 0.044, 0.748, 0.65, -0.011, -0.069, 0.424]
seed5 = [-0.166, 0.751, 0.761, 0.285, -0.119, 0.738, 0.802, -0.02, 0.004, 0.424,
         0.268, -0.047, 0.161, 0.291, 0.347, 0.368, 0.003, 0.182, 0.815, -0.021,
         0.677, 0.206, 0.627, 0.605, 0.756, 0.689, 0.079, -0.028, 0.559, -0.061,
         -0.126, 0.477, 0.255, 0.683, 0.355, 0.445, 0.6, -0.046, 0.669, -0.105,
         -0.111, 0.301, -0.087, -0.001, 0.175, 0.375, 0.285, 0.398, -0.157, 0.663]
seed6 = [0.035, 0.155, -0.156, 0.635, 0.253, 0.072, 0.688, -0.009, 0.804, 0.119,
         0.028, 0.632, -0.116, 0.181, 0.517, 0.622, -0.074, 0.338, -0.152, 0.388,
         0.202, 0.461, 0.58, 0.011, 0.643, 0.067, 0.576, -0.101, 0.725, 0.024,
         0.661, 0.754, -0.168, 0.064, 0.741, 0.285, -0.007, 0.172, 0.236, 0.629,
         -0.002, 0.659, 0.423, 0.455, -0.038, 0.125, 0.373, 0.068, 0.219, 0.768]
seed7 = [0.342, 0.118, 0.242, 0.237, 0.157, 0.549, 0.048, 0.552, 0.88, 0.405,
         0.401, 0.443, 0.132, -0.17, 0.788, 0.549, -0.124, 0.509, 0.768, 0.732,
         0.033, -0.127, -0.084, 0.332, 0.173, 0.522, 0.874, 0.486, 0.298, 0.023,
         0.724, -0.093, -0.044, 0.838, -0.057, -0.165, 0.455, -0.15, 0.292,
         -0.145, 0.47, 0.415, 0.781, 0.07, -0.083, 0.422, 0.299, 0.459, 0.042, -0.026]
seed8 = [-0.052, -0.005, 0.263, 0.366, 0.318, 0.772, 0.444, 0.547, -0.035, 0.033,
         0.653, 0.366, 0.6, 0.167, 0.673, 0.396, 0.443, 0.716, 0.286, 0.163, 0.188,
         -0.083, 0.71, -0.051, 0.841, 0.838, -0.126, -0.135, -0.02, -0.013, 0.201,
         0.625, -0.099, 0.379, 0.237, 0.121, 0.408, -0.023, 0.7, -0.091, -0.069,
         -0.138, 0.22, 0.474, -0.092, 0.599, 0.688, 0.892, 0.123, 0.418]
seed9 = [0.021, -0.026, 0.167, 0.41, 0.256, 0.616, 0.247, 0.216, 0.882, 0.407,
         0.763, 0.239, 0.484, 0.026, 0.547, 0.396, -0.157, 0.038, -0.025, 0.391,
         0.39, 0.702, -0.002, 0.712, 0.149, 0.054, -0.166, 0.504, 0.058, 0.295,
         0.408, 0.182, 0.591, 0.297, 0.799, 0.396, 0.356, 0.183, 0.136, -0.084,
         0.519, 0.074, 0.59, -0.17, 0.186, 0.632, 0.472, -0.089, 0.631, 0.136]
seed10 = [-0.057, 0.544, -0.166, 0.352, 0.261, -0.062, -0.142, 0.004, -0.028,
          -0.152, 0.731, 0.047, 0.785, 0.626, 0.158, 0.576, 0.804, -0.079,
          0.85, 0.436, 0.457, 0.218, 0.39, 0.31, 0.583, 0.235, 0.829, -0.149,
          0.307, -0.104, 0.413, 0.439, 0.553, -0.074, 0.886, -0.134, 0.303,
          -0.135, 0.317, 0.284, 0.099, 0.061, 0.018, 0.194, 0.889, 0.267,
          0.315, 0.717, -0.036, 0.382]

residue_probs = [0.983, 0.500, 0.498, 0.138, 0.500,
                 0.692, 0.682, 0.691, 0.693, 0.491,
                 0.137, 0.171, 0.798, 0.815, 0.812,
                 0.979, 0.498, 0.500, 0.500, 0.500,
                 0.500, 0.500, 0.500, 0.500, 0.498,
                 0.497, 0.500, 0.500, 0.499, 0.500,
                 0.974, 0.791, 0.500, 0.500, 0.829,
                 0.987, 0.497, 0.776, 0.805, 0.971,
                 0.498]

residue_escape = [1]*50
seedingCells = [seed1, seed2, seed3, seed4, seed5, seed6, seed7, seed8, seed9, seed10]

with open('output/seedingCells.csv', 'w') as output:
    w = csv.writer(output)
    w.writerow([f'res{i}' for i in range(50)])
    w.writerows(seedingCells)