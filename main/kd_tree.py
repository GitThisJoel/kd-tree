from random_points import random_points

class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.right = right
        self.left = left

    def __str__(self):
        l0 = f"  {self.value}"
        if not (self.right == None or self.left == None):
            l1 = " / \ "
            l2 = f"{self.left.value}  {self.right.value}"
        elif self.left == None:
            l1 = "   \ "
            l2 = f"      {self.right.value}"
        elif self.left == None:
            l1 = " /     "
            l2 = f"{self.left.value}"
        return f"{l0}\n{l1}\n{l2}"


n1 = Node(3, None, None)
n2 = Node(14, None, None)
n3 = Node(7, n1, n2)

print(n3)
