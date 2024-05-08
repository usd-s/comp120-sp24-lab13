# File: linkedlist.py
# Date: TODO
# Author: TODO

# Write the definition of a method of the LinkedList class called get_center
# that returns the central node of the list.
from typing import Any


class LinkedListNode:

    def __init__(self, item: Any, next=None):
        self.item = item
        self.next = next


class LinkedList:

    def __init__(self):
        self.front: LinkedListNode = None

    def __str__(self):
        s = ''
        n = self.front
        while n:
            s += str(n.item) + ' '
            n = n.next
        return s

    def add(self, val) -> None:
        """ add <val> as the last node """
        if not self.front:
            self.front = LinkedListNode(val)
        else:
            n = self.front
            while n.next:
                n = n.next
            n.next = LinkedListNode(val)

    def get_center(self):
        """ return a reference to the center node """
        # TODO
        ...


if __name__ == '__main__':
    # test code
    l = LinkedList()
    for i in range(1, 6):
        l.add(i)

    print("\nTest #1:")
    print("Should print out 3")
    c_value = l.get_center().item
    print("You are printing out", c_value)
    if c_value == 3:
        print("Test #1 Passed")
    else:
        print("You don't have the expected result. Keep working on it.")

    l.add(6)
    c_value = l.get_center()
    print("\nTest #2:")
    print("Should print out 4")
    c_value = l.get_center().item
    print("You are printing out", c_value)
    if c_value == 4:
        print("Test #2 Passed")
    else:
        print("You don't have the expected result. Keep working on it.")
