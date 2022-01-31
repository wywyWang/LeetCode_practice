from typing import Optional


def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    '''
    Time: O(logn), Space: O(1)
    '''
    global targetSum
    # edge case
    if not root:
        return False
    # edge case: only root
    if not root.left and not root.right:
        if root.val == targetSum:
            return True
        else:
            return False

    if root.left:
        match = DFS(root.left, root.val)
        if match:
            return True
    if root.right:
        match = DFS(root.right, root.val)
        if match:
            return True
    return False


def DFS(root: Optional[TreeNode], path_sum: int) -> bool:
    if not root.left and not root.right:
        if root.val + path_sum == targetSum:
            return True
        else:
            return False
    if root.left:
        match_left = DFS(root.left, root.val+path_sum)
    else:
        match_left = False
    if root.right:
        match_right = DFS(root.right, root.val+path_sum)
    else:
        match_right = False
    return (match_left or match_right)