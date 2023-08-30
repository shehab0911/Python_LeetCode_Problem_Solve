class Solution(object):
    def removeDuplicates(self, nums):
        nums[:] = list(set(nums))
        nums.sort()
        return len(nums)

r =[1,3,2,1,4,2,2]

obj = Solution()
x=obj.removeDuplicates(r)
print(x)