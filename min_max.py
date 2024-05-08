# File: binarytree.py
# Date: TODO
# Author: TODO

from typing import Any


class BinaryTreeNode:

    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        """ 
        Returns string representation of the node,
        with just the value stored in the node.
        """
        return str(self.val)


class BSTree:
    root: BinaryTreeNode | None

    def __init__(self, r: BinaryTreeNode = None):
        self.root = r

    def get_max(self) -> int | None:
        """ returns the largest value in the BSTree
            If no node in the tree, return None """
        # TODO Provide your solution
        pass

    def get_min(self) -> int | None:
        """ returns the smallest value in the tree
            If no node in the tree returns None
        """
        # TODO Provide your solution
        pass


if __name__ == "__main__":
    # Create tree nodes
    a = BinaryTreeNode(1)
    c = BinaryTreeNode(3)
    b = BinaryTreeNode(2, a, c)
    d = BinaryTreeNode(4, b, None)
    l = BinaryTreeNode(11)
    k = BinaryTreeNode(10, None, l)
    p = BinaryTreeNode(15)
    o = BinaryTreeNode(14, None, p)
    m = BinaryTreeNode(12, k, o)
    i = BinaryTreeNode(8, d, m)
    tree = BSTree(i)
    result = (tree.get_max(), tree.get_min())
    print("    Expected: (15, 1)")
    print('Your result: ', result)
    if result == (15, 1):
        print("Passed Test")
    if result[0] != 15:
        print("Max value is incorrect.")
    if result[1] != 1:
        print("Min value is incorrect. ")
