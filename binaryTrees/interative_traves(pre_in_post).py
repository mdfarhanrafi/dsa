class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def preOrder_iterative(root):
    if root is None:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.data)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


def inOrder_iterative(root):
    if root is None:
        return []

    stack = []
    result = []
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        result.append(current.data)
        current = current.right

    return result


# post oder using 2 stacks
def postOrder_iterative(root):
    if root is None:
        return []

    stack1 = [root]
    stack2 = []
    result = []

    while stack1:
        node = stack1.pop()
        stack2.append(node)

        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    while stack2:
        node = stack2.pop()
        result.append(node.data)

    return result

# post order using single stack


def postOrder_iterative_single_stack(root):
    if root is None:
        return []

    stack = []
    result = []
    last_visited = None
    current = root

    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                result.append(peek_node.data)
                last_visited = stack.pop()

    return result
