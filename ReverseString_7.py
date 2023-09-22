class Solution(object):
    def reverse(self, x):
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31

        result = 0
        sign = 1 if x > 0 else -1
        x = abs(x)

        while x != 0:
            pop = x % 10
            x //= 10

            if result > INT_MAX // 10 or (result == INT_MAX // 10 and pop > 7):
                return 0

            result = result * 10 + pop

        return sign * result


obj = Solution()
result = obj.reverse(123)
print(result)
