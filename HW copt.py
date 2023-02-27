points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}

def calculate_distance(coordinates):
    dist=0.0
    for i in range (1, len(points)):
        ends = points[(coordinates[i-1], coordinates[i])]
        dist += points [(min(ends), max(ends))]
    
    return dist
    print (dist)

calculate_distance ([0, 1, 3, 2, 0])