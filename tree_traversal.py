# File: treetraversal.py
# Date: TODO
# Author: TODO

...

from typing import Any


class TreeNode:

    def __init__(self, val: Any) -> None:
        self.val = val
        self.children = []

    def add_children(self, new_children: list):
        self.children.extend(new_children)


class Tree:

    def __init__(self, root: TreeNode = None) -> None:
        self.root = root

    def breath_first_traversal(self) -> None:
        """ print nodes in breath-first order 
            one level at a line
        """
        
        # TODO Provide your solution
        pass


if __name__ == '__main__':
    nodes = {x: TreeNode(x.upper()) for x in 'abcdefgjhijklmn'}

    nodes['a'].add_children([nodes['b'], nodes['c'], nodes['d']])
    nodes['b'].add_children([nodes['e'], nodes['f']])
    nodes['c'].add_children([nodes['g']])
    nodes['d'].add_children([nodes['h'], nodes['i'], nodes['j'], nodes['k']])
    nodes['e'].add_children([nodes['l']])
    nodes['j'].add_children([nodes['m']])
    nodes['m'].add_children([nodes['n']])
    tree = Tree(nodes['a'])
    tree.breath_first_traversal()
