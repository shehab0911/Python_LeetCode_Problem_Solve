from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0
        stack=[root]
        result=[]

        while stack:
            
            for _ in range(len(stack)):
                node=stack.pop()
                result.append(node)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return len(result)

        
        
        
        