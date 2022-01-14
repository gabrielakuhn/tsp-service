import math
import numpy as np

def euclidean_distance(lat_from, lon_from, lat_to, lon_to):
    """Method to compute euclidean distance"""
    return math.sqrt((lat_from - lat_to) ** 2 + (lon_from - lon_to) ** 2)

def compute_distance_matrix(loc):
    """Method to create a matrix with locations distance"""

    my_array = np.array(loc)
    n = len(loc)
    distance_matrix = []
    for i in range(n):
        distance_arr = []
        lat_from = float(my_array[i]["lat"])
        lon_from = float(my_array[i]["lon"])
        for j in range(n):
            lat_to = float(my_array[j]["lat"])
            lon_to = float(my_array[j]["lon"])
            distance = int(euclidean_distance(lat_from, lon_from, lat_to, lon_to))
            distance_arr.append(distance)
        distance_matrix.append(distance_arr)
    return (distance_matrix)