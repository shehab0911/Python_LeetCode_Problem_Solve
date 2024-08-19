class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        
        
        temp = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(temp)
        
        return root


def print_tree(root):
    if root is not None:
        print_tree(root.left)
        print(root.val, end=' ')
        print_tree(root.right)

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

solution = Solution()
inverted_root = solution.invertTree(root)

print("Original tree :")
print_tree(root)
print("Inverted tree :")
print_tree(inverted_root)
