class Solution(object):
    def maxSubArray(self, nums):
        current_sum=0
        max_sum=-1000000000000000

        for i in nums:
            current_sum+=i
            max_sum=max(current_sum,max_sum)
            if current_sum<0:
                current_sum=0
        return max_sum
        
        