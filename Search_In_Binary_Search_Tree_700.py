# Problem: 700. Search in a Binary Search Tree
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if not root:
            return None
        elif root.val==val:
            return root
        elif val<root.val:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
    def print_all(self,root):
        if root:
            print(root.val)
            if root.left:
                print(root.left.val)
            if root.right:
                print(root.right.val)
            
root=TreeNode(4)
root.left=TreeNode(2)
root.right=TreeNode(7)
root.left.left=TreeNode(1)
root.left.right=TreeNode(3)
s=Solution()
s.print_all(s.searchBST(root,2))

    

       