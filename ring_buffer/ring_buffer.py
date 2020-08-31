
from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        else:
            if self.current is None or self.current.next is None:
                self.current = self.storage.head
            else:
                self.current = self.current.next
            self.current.value = item
            

    def get(self):
        buffer = []
        node = self.storage.head
        while node is not None:
            buffer.append(node.value)
            node = node.next

        return buffer