class Solution(object):
    def targetIndices(self, nums, target):
        list1=[]
        nums.sort()
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                i=mid
                while i>=0 and nums[i]==target:
                    i-=1
                j=mid
                while j<len(nums) and nums[j]==target:
                    j+=1
                return list(range(i+1,j))
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return []
        """nums.sort()
        list1=[]
        for x in range(len(nums)):
            if nums[x] == target :
                list1.append(x)
        return list1"""
        
        
        