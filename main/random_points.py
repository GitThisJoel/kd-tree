import random

def random_points(n: int, dim: int = 2, ranges: [(int, int)] = None):
    if ranges == None:
        ranges = [(0,1)] * dim
    elif len(ranges) < dim:
        print("WARNING: the number of ranges do not match to number of dimensions in gen_random_points.")
        ranges += [rnages[-1]] * (dim - len(ranges))

    points = [0] * n
    for i in range(n):
        p = [0] * dim
        for j in range(len(ranges)):
            coord = random.uniform(*ranges[j])
            p[j] = coord
        points[i] = tuple(p)

    return points
