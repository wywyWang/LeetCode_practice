import argparse
from queue import Queue
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        '''
        Space: O(n), time: O(nlogn)
        '''
        bst = None
        for node in preorder:
            if bst is None:
                bst = TreeNode(node)
            else:
                self._insert(bst, node)

        return bst

    def _insert(self, tree, node):
        if node < tree.val:
            if tree.left is None:
                tree.left = TreeNode(node)
            else:
                self._insert(tree.left, node)
        else:
            if tree.right is None:
                tree.right = TreeNode(node)
            else:
                self._insert(tree.right, node)


def get_argument():
    opt = argparse.ArgumentParser()
    opt.add_argument("--preorder",
                        type=int,
                        nargs='+',
                        required=True,
                        help="an array of integers preorder")
    config = vars(opt.parse_args())
    return config


if __name__ == '__main__':
    inputs = get_argument()
    sol = Solution()

    ans = sol.bstFromPreorder(inputs['preorder'])

    # test the results
    q = Queue()
    q.put(ans)
    while not q.empty():
        current_node = q.get()
        print(current_node.val)
        if current_node.left is not None:
            q.put(current_node.left)
        if current_node.right is not None:
            q.put(current_node.right)