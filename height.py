# File: binarytree.py
# Date: TODO
# Author: TODO

# from typing import Any, Optional
from collections import deque


class BinaryTreeNode:

    def __init__(self, val: int, left=None, right=None) -> None:
        """ 
        Initialize the node with a value,
        with left child from the parameter left 
        and the right child from the parameter right.
        """
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def __init__(self, root: BinaryTreeNode = None) -> None:
        """ 
        Initialize the root of the tree
        from the parameter root.
        """
        self.root = root

    def size(self) -> int:
        """ returns the number of nodes in the tree"""
        return self._size(self.root)

    def _size(self, node: BinaryTreeNode | None):
        """ recursive helper method to size()"""
        # base case
        if node is None:
            return 0
        # divide and conquer
        current_node_count = 1
        left_node_count = self._size(node.left)
        right_node_count = self._size(node.right)
        # combine
        return current_node_count + left_node_count + right_node_count

    def height(self) -> int:
        """ returns the height of the tree"""
        
        # TODO
        ...


if __name__ == "__main__":
    # Create tree nodes
    d = BinaryTreeNode(4)
    g = BinaryTreeNode(7)
    j = BinaryTreeNode(10)
    k = BinaryTreeNode(11)
    m = BinaryTreeNode(13)
    h = BinaryTreeNode(8, j, k)
    l = BinaryTreeNode(12, None, m)
    i = BinaryTreeNode(9, None, l)
    e = BinaryTreeNode(5, g, h)
    f = BinaryTreeNode(6, None, i)
    b = BinaryTreeNode(2, d, e)
    c = BinaryTreeNode(3, f)
    a = BinaryTreeNode(1, b, c)

    # Create tree
    tree = BinaryTree(a)

    print('Size: ', tree.size())
    print('Height: ', tree.height())
    if tree.height() == 5:
        print("\tPassed test.")
    else:
        print('\tIncorrect. Keep working on it')
