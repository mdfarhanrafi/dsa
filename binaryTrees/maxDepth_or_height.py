

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


def maxDepth(root):
    if root is None:
        return 0
    lh = maxDepth(root.left)
    rh = maxDepth(root.right)
    return 1 + max(lh, rh)


print(maxDepth(root))  # Output: 3
