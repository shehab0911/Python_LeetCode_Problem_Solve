class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        list1=[1]*n

        left_element=1
        for i in range(len(nums)):
            list1[i]=left_element
            left_element*=nums[i]
        right_element=1
        for i in range(n-1,-1,-1):
            list1[i]*=right_element
            right_element*=nums[i]
        return list1
        
        