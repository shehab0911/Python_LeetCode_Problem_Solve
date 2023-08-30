class Solution(object):
    def containsDuplicate(self, nums):

        list=set(nums)

        for i in nums:
            if i in list:
                return True
            else:
                return False


r = [1, 3, 2, 1, 4, 2, 2]
obj = Solution()
x = obj.containsDuplicate(r)
print(x)
