from random_points import random_points

from dataclasses import dataclass
from typing import TypeVar

Node = TypeVar('Node')

@dataclass
class Node:
    value: int
    left: Node = None
    right: Node = None

def create_kd_tree(points, depth):
    return

if __name__ == "__main__":
    a = Node(10)
    b = Node(20)
    c = Node(value=30, left=a, right=b)
    print(c)
