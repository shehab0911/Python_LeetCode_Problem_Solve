class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root):
        result = []
        self.rpreorder(root, result)
        return result

    def rpreorder(self, root, result):
        if root:
            result.append(root.val)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)


# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
solution = Solution()
print(solution.preorderTraversal(root))  # Output: [1, 3, 2]
