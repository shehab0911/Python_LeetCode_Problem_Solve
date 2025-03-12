class Solution(object):
    def singleNumber(self, nums):
        dict={ }
        for x in nums:
            if x in dict:
                dict[x]+=1
            else:
                dict[x]=1
        for key ,values in dict.items():
            if values==1:
                return key
      