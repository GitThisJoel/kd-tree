from random_points import random_points

from dataclasses import dataclass
from typing import TypeVar

Node = TypeVar('Node')

@dataclass
class Node:
    location: tuple
    left: Node = None
    right: Node = None

def kd_tree(points, depth):
    k = len(points[0])
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    
    median = len(points)//2
    return Node(
            location=points[median],
            left=points[:median],
            right=points[median+1:]
        )

if __name__ == "__main__":
    a = Node((1,2))
    b = Node((3,4))
    c = Node(location=(5,6), left=a, right=b)
    print(c)
