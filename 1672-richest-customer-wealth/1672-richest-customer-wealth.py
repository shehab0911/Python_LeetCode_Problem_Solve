class Solution(object):
    def maximumWealth(self, accounts):
        list1=[]
        for x in accounts:
            list1.append(sum(x))
        return max(list1)
        
        