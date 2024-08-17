class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        result = []
        self.rinorder(root, result)
        return result

    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.val)
            self.rinorder(root.right, result)


# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
solution = Solution()
print(solution.inorderTraversal(root))  # Output: [1, 3, 2]
