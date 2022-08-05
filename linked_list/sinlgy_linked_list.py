from typing import List


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get_length(self) -> int:
        return self.length

    def add_to_tail(self, value) -> None:
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
        else:
            node = Node(value)
            self.tail.next = node
            self.tail = node
            self.length += 1

    def create_from_list(self, arr: List) -> None:
        for element in arr:
            self.add_to_tail(element)

    def add_to_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1

    def remove_from_head(self):
        self.head = self.head.next
        self.length -= 1

    def print_list(self) -> None:
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.next
        print()


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.create_from_list([i for i in range(34, 101)])
    breakpoint()
