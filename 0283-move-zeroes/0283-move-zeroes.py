class Solution(object):
    def moveZeroes(self, nums):
        list1 = []
        list2 = []

        for i in nums:
            if i == 0:
                list1.append(i)
            else:
                list2.append(i)

        nums[:] = list2 + list1