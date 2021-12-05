import argparse
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    def rob(self, root: Optional[TreeNode]) -> int:
        '''
        Given the root of the binary tree
        Return the maximum amount of money the thief can rob without alerting the police.
        Left: rob given node -> node.val + children's children max(rob or not rob)
        Right: don't rub given node -> children's max(rob or not rob)
        '''

        def DFS(root):
            if not root:
                return 0, 0

            left_left, left_right = DFS(root.left)
            right_left, right_right = DFS(root.right)
            return root.val+left_right+right_right, max(left_left, left_right)+max(right_left, right_right)

        left_money, right_money = DFS(root)
        return max(left_money, right_money)
        

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
    print(sol.rob(tree.root))