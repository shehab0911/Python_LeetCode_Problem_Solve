from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        if root is None:
            return []
        queue=deque([root])
        result=[]

        while queue:
            level=0
            for _ in range(len(queue)):
                node=queue.popleft()
                level+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        v=max(result)
        return result.index(v)+1
        

            
            
            



        
       
        