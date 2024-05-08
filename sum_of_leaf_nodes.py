# File: tree.py
# Date: TODO
# Author: TODO

from typing import Any


class TreeNode:

    def __init__(self, val: int) -> None:
        self.val = val
        self.children = []

    def add_children(self, new_children: list) -> None:
        self.children.extend(new_children)


class Tree:

    def __init__(self, root: TreeNode = None) -> None:
        self.root = root

    def sum_of_leaf_nodes(self) -> int:
        """ Returns sum of leaf nodes in tree. """
        # TODO provide your solution
        ...


if __name__ == "__main__":
    # Create a tree
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)

    n1.add_children([n2, n3, n4])
    n3.add_children([n5, n6])
    n4.add_children([n7])
    n5.add_children([n8, n9])

    tree = Tree(n1)

    sum = tree.sum_of_leaf_nodes()
    print("\nTesting sum_of_leaf_nodes() method")
    print("Should print 32")
    print("Sum of leaf nodes = ", sum)

    if sum == 32:
        print("Passed test")
    else:
        print("Incorrect, keep working on it")
