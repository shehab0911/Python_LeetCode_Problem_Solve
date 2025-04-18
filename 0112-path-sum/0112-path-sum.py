from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """def path(root,cur_sum):
            if root is None:
                return False
            cur_sum+=root.val
            if root.left is None and root.right is None:
                return cur_sum==targetSum
            return (path(root.left,cur_sum) or path(root.right,cur_sum))
        return path(root,0)"""
        if root is None:
            return False
        stack=[(root,root.val)]

        while stack:
            node,cur_sum=stack.pop()
            if node.left is None and node.right is None and cur_sum==targetSum:
                return True
            if node.left:
                stack.append((node.left,cur_sum + node.left.val))
            if node.right:
                stack.append((node.right,cur_sum + node.right.val))
        return False

       
        
      
        