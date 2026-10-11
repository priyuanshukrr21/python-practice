class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def has_cycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = b  # Creates a cycle

print(has_cycle(a))