class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):  # Use 'range' to iterate over indices
            for j in range(i + 1, len(nums)):  # Start inner loop from i + 1
                if nums[i] + nums[j] == target:
                    return [i, j]

num = [2, 7, 11, 15]
obj = Solution()
result = obj.twoSum(num, 13)
print(result)