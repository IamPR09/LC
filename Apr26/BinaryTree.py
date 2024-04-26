"""
Implement a binary tree that looks like this :


             1
            / \
           2   3
          /
         4
"""


class Node :
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
