class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to print the linked list


def printLL(head):
    while head is not None:
        print(head.data, end=' ')
        head = head.next

# Function to delete the Nth node from the end of the linked list


def DeleteNthNodefromEnd(head, N):
    # Create two pointers, fastp and slowp
    fastp = head
    slowp = head

    # Move the fastp pointer N nodes ahead
    for i in range(N):
        fastp = fastp.next

    # If fastp becomes None, the Nth node from the end is the head
    if fastp is None:
        return head.next

    # Move both pointers until fastp reaches the end
    while fastp.next is not None:
        fastp = fastp.next
        slowp = slowp.next

    # Delete the Nth node from the end
    delNode = slowp.next
    slowp.next = slowp.next.next
    delNode = None
    return head


arr = [1, 2, 3, 4, 5]
N = 3
head = Node(arr[0])
head.next = Node(arr[1])
head.next.next = Node(arr[2])
head.next.next.next = Node(arr[3])
head.next.next.next.next = Node(arr[4])

# Delete the Nth node from the end and print the modified linked list
head = DeleteNthNodefromEnd(head, N)
printLL(head)
