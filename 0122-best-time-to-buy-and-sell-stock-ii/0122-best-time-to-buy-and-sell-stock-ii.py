class Solution(object):
    def maxProfit(self, prices):
        list1=[]
        i=0
        j=1
        while i<len(prices) and j<len(prices):
            if prices[j]>prices[i]:
                sum1=prices[j]-prices[i]
                list1.append(sum1)
                i+=1
                j+=1
            else:
                j+=1
                i+=1

        return sum(list1)
            
        
        
        