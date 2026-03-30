class Solution(object):
    def maxSubarraySumCircular(self, nums):
        globMax=nums[0]
        globMin=nums[0]
        curMin=0
        curMax=0
        total=0

        for i in nums:
            curMax=max(curMax+i,i)
            curMin=min(curMin+i,i)
            total+=i
            globMax=max(globMax,curMax)
            globMin=min(globMin,curMin)
        return max(globMax,total-globMin) if globMax>0 else globMax
      
        
        
       
       

        
        
      
      