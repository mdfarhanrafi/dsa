class Node:
    def __init__(self, data1, next1=None):
        self.data = data1
        self.next = next1

# Function to check if a given element is present in the linked list


def check_if_present(head, desired_element):
    temp = head

    # Traverse the linked list
    while temp is not None:
        # Check if the current node's data is equal to the desired element
        if temp.data == desired_element:
            return 1  # Return 1 if the element is found

        # Move to the next node
        temp = temp.next

    return 0  # Return 0 if the element is not found in the linked list


# Main function
if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3
    arr = [1, 2, 3]
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])

    val = 3  # Element to be checked for presence in the linked list

    # Call the check_if_present function and print the result
    print(check_if_present(head, val))
