class Node:
    def __init__(self, data, next1=None):
        self.data = data
        self.next = next1


head = Node(1)
head.next = next_node = Node(2)

temp = head
while temp.next is not None:
    print(f"{temp.data} -> ", end="")
    temp = temp.next


print(head.data)
