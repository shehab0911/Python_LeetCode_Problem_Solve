class Solution(object):
    def findMiddleIndex(self, nums):
        totalSum=sum(nums)
        prevSum=0

        for i in range(len(nums)):
            rightSum=totalSum-nums[i]-prevSum
            if prevSum==rightSum:
                return i
            prevSum+=nums[i]
        return -1
        
        