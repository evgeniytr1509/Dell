points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    distance = 0.0

    for i in range(1, len(coordinates)):
        ends = (coordinates[i-1], coordinates[i])
        distance += points[(min(ends), max(ends))]

    return distance

calculate_distance (points, 2)