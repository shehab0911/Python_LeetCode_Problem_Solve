class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        list1=[]
        for x in range(len(nums)):
            if nums[x] == target or x in list1:
                list1.append(x)
        return list1
        
        
        