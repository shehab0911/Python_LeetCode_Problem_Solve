class Solution(object):
    def increasingTriplet(self, nums):
        
        """for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i]<nums[i+1]:
                return True
            nums[i]=1
        return False"""

        first =second= float('inf')
        

        for num in nums:

            if num <= first:
                first = num

            elif num <= second:
                second = num

            else:
                return True

        return False

