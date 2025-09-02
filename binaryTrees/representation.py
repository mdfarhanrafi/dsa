from collections import deque


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


def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')

    else:
        return


def pre_order_traversal(node):
    if node is not None:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

    else:
        return


def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)

    else:
        return


# level order_traversal(root)
class Solution:
    def levelOrder(self, root):
        # Create a list to store levels
        ans = []
        if not root:
            # If the tree is empty,
            # return an empty list
            return ans

        # Create a queue to store nodes
        # for level-order traversal
        q = deque()
        # Enqueue the root node
        q.append(root)

        while q:
            # Get the size of the current level
            size = len(q)
            # Create a list to store
            # nodes at the current level
            level = []

            for i in range(size):
                # Get the front node in the queue
                node = q.popleft()
                # Store the node value
                # in the current level list
                level.append(node.val)

                # Enqueue the child nodes if they exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Store the current level
            # in the answer list
            ans.append(level)
        # Return the level-order
        # traversal of the tree
        return ans

# Function to print
# the elements of a list


def printList(lst):
    # Iterate through the
    # list and print each element
    for num in lst:
        print(num, end=" ")
    print()


post_order_traversal(root)
print()  # For better readability
pre_order_traversal(root)
print()  # For better readability
in_order_traversal(root)
print()  # For better readability
