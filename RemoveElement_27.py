class Solution(object):
    def removeElement(self, nums: list[int], val: int) -> int:

        new_length = 0

        for num in nums:
            if num != val:
                nums[new_length] = num
                new_length += 1

        return new_length


obj = Solution()
result = obj.removeElement([3, 2, 2, 3], 3)
print(result)





