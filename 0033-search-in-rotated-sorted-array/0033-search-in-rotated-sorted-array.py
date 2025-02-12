class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        mid_index=0

        while left<=right:
            mid_index=(left+right)//2

            if nums[mid_index]==target:
                return mid_index
            if nums[left]<=nums[mid_index]:
                if nums[left]<=target<nums[mid_index]:
                    right=mid_index-1
                else:
                    left=mid_index+1
            else:
                if nums[mid_index]<target<=nums[right]:
                    left=mid_index+1
                else:
                    right=mid_index-1

        return -1

        