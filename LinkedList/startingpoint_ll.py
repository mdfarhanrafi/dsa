class Node:
    def __init__(self, data, next_node=None):
        # Data stored in the node
        self.data = data
        # Pointer to the next node in the list
        self.next = next_node

# Function to find the first
# node of the loop in a linked list


def first_node(head):
    # Initialize a slow and fast
    # pointers to the head of the list
    slow = head
    fast = head

    # Phase 1: Detect the loop
    while fast is not None and fast.next is not None:
        # Move slow one step
        slow = slow.next

        # Move fast two steps
        fast = fast.next.next

        # If slow and fast meet,
        # a loop is detected
        if slow == fast:
            # Reset the slow pointer
            # to the head of the list
            slow = head

            # Phase 2: Find the first
            # node of the loop
            while slow != fast:
                # Move slow and fast one
                # step at a time
                slow = slow.next
                fast = fast.next

                # When slow and fast meet again,
                # it's the first node of the loop
            return slow

    # If no loop is found, return None
    return None


# with a loop
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node3 = Node(3)
node2.next = node3
node4 = Node(4)
node3.next = node4
node5 = Node(5)
node4.next = node5

# Make a loop from node5 to node2
node5.next = node2

# Set the head of the linked list
head = node1

# Detect the loop in the linked list
loop_start_node = first_node(head)

if loop_start_node:
    print("Loop detected. Starting node of the loop is:", loop_start_node.data)
else:
    print("No loop detected in the linked list.")
