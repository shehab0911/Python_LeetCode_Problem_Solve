class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        result = []
        self.rpostorder(root, result)
        return result

    def rpostorder(self, root, result):
        if root:
            
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.val)


# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
solution = Solution()
print(solution.postorderTraversal(root))  # Output: [1, 3, 2]
