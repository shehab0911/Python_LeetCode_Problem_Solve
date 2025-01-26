class Solution(object):
    def longestConsecutive(self, nums):
        list1=[]
        num = list(set(nums))
        num.sort()

        max_length=1
        current_num=1
        for x in range(1, len(num)):
            if num[x] - num[x - 1]==1:
                current_num+=1
                max_length=max(max_length,current_num)
            else:
                current_num=1

        return max_length



        