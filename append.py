# File: linkedlist.py
# Date: TODO
# Author: TODO

# Write the definition of a method of the LinkedList class called append
# that adds the passed in value to the last node.

from typing import Any


class LinkedListNode:

    def __init__(self, val: Any, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.front: LinkedListNode = None
        self.size: int = 0

    def __str__(self):
        s = ''
        n = self.front
        while n:
            s += str(n.val) + ' '
            n = n.next
        return s + 'with size of ' + str(self.size)

    def append(self, val) -> int:
        """ add <val> as the last node """
        
        # TODO Provide your solution
        pass



if __name__ == '__main__':
    # test code
    c = LinkedListNode('c')
    b = LinkedListNode('b', c)
    a = LinkedListNode('a', b)
    l = LinkedList()
    l.front = a
    l.size = 3
    l.append('d')
    l1 = LinkedList()
    l1.append('a')
    print("\nTest1:")
    print('Expected result: a with size of 1')
    print('    Your result: ', end='')
    print(l1)
    if str(l1) == 'a with size of 1':
        print("Test1 passed")
    else:
        print("Test1 Incorrect. Continue working on it. ")

    print("\nTest2:")
    print('Expected result: a b c d with size of 4')
    print('    Your result: ', end='')
    print(l)
    if str(l) == 'a b c d with size of 4':
        print("Test2 passed")
    else:
        print("Test2 Incorrect. Continue working on it. ")

