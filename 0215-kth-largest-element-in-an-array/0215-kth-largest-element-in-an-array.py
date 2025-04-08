class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort()
        n=len(nums)-k
        return nums[n]

       
        