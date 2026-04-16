class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

current = head
while current:
    print(current.val, end="->")
    current = current.next
print("None")