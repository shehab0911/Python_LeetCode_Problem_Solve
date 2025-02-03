class Solution(object):
    def moveZeroes(self, nums):
        #nums.sort()
        i = 0
        j = len(nums) - 1


        for j in range(len(nums)):
            if nums[j]!=0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        return nums

nums = [0,1,0,3,12]
obj=Solution()
result=obj.moveZeroes(nums)
print(result)

