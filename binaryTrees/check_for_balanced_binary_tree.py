
# for every node, check if the height of left and right subtree differ by at most 1
# time complexity: O(n^2) in worst case (skewed tree)
# space complexity: O(h) where h is the height of the tree (recursion stack)


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
    if lh == -1:
        return -1
    rh = maxDepth(root.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    return 1 + max(lh, rh)


def isBalanced(root):

    return maxDepth(root) != -1


print(isBalanced(root))  # Output: True
