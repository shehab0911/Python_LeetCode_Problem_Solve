class Solution(object):
    def applyOperations(self, nums):
        n=len(nums)
        j=1
        for i in range(1,n):
            if nums[i]==[i+1]:
                nums[j]=nums[i]+nums[i-1]
                j+=1
        return nums[j]
        