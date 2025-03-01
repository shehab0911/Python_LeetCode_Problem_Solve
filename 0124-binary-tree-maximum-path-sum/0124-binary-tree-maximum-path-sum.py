# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        res=[float('-inf')]

        def dfs(root):
            if root is None:
                return 0
            left_side=dfs(root.left)
            right_side=dfs(root.right)
            left_side=max(left_side,0)
            right_side=max(right_side,0)

            res[0]=max(res[0],root.val,left_side,right_side)
            return root.val + max(left_side,right_side)
        dfs(root)
        return res[0]

       
        