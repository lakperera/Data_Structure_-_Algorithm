class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = ListNode(value)
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = ListNode(value)

    def print(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

list = LinkedList()
for i in range(10):
    list.append(i)
list.append(1)
list.append(2)
list.print()
