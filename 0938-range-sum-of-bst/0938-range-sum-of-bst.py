# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        if root is None:
            return []
        stack=[root]
        result=[]

        while stack:
            for _ in range(len(stack)):
                node=stack.pop()
                result.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        list1=[]
        for i in result:
            if i>=low and i<=high:
                list1.append(i)
        return sum(list1)


    
        