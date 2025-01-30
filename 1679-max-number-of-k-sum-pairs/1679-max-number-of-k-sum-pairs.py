class Solution(object):
    def maxOperations(self, nums, k):
        count=0
        i=0
        j=len(nums)-1
        nums.sort()
        while i<j:
            summ= nums[i]+nums[j]
            if summ==k:
                count+=1
                i+=1
                j-=1
            elif nums[i]+nums[j]<k:
                i+=1
            else:
                j-=1
        return count
            
    
        