class Solution(object):
    def isPalindrome(self, x):
        x_str = str(x)

        return x_str == x_str[::-1]


obj = Solution()

print(obj.isPalindrome(121))
