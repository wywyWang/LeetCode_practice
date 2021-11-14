import argparse
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinarySearchTree:
    # unused for the problem
    def __init__(self, inputs):
        self.root = None
        self.insert(inputs)

    def insert(self, inputs):
        for node in inputs:
            if self.root == None:
                self.root = TreeNode(node)
            else:
                self._insert(self.root, node)

    def _insert(self, current_node, node):
        if node <= current_node.val:
            if current_node.left is None:
                current_node.left = TreeNode(node)
            else:
                self._insert(current_node.left, node)
        else:
            if current_node.right is None:
                current_node.right = TreeNode(node)
            else:
                self._insert(current_node.right, node)


class BinaryTree:
    def __init__(self, inputs):
        self.root = None
        self.insert(inputs)

    def insert(self, inputs):
        for node in inputs:
            if self.root is None:
                self.root = TreeNode(node)
            else:
                self._insert(self.root, node)

    def _insert(self, current_node, value):
        # insert rule: from left to right
        if current_node.left is None:
            current_node.left = TreeNode(value)
        elif current_node.right is None:
            current_node.right = TreeNode(value)
        else:
            if not current_node.left.left or not current_node.left.right:
                self._insert(current_node.left, value)
            else:
                self._insert(current_node.right, value)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            raise NotImplementedError

        # sol: use tree height, space: O(N), time: O(N+E)
        diameter = 0
        def DFS(root):
            nonlocal diameter           # global variable
            if not root:                # node may be empty
                return 0

            left_depth = DFS(root.left)
            right_depth = DFS(root.right)
            diameter = max(diameter, left_depth+right_depth)

            return 1 + max(left_depth, right_depth)
        
        DFS(root)
        return diameter


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--root",
                        type=int,
                        nargs='+',
                        required=True,
                        help="binary tree")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()
    tree = BinaryTree(inputs['root'])
    print(sol.diameterOfBinaryTree(tree.root))