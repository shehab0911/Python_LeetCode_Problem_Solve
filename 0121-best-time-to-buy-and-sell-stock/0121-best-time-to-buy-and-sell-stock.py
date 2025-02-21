class Solution(object):
    def maxProfit(self, prices):
        """max_profit = 0
       
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                subt = prices[j] - prices[i]
                if subt > max_profit:
                    max_profit=subt


        return max_profit"""
        left=0
        right=1
        max_Profit=0
        while right<len(prices):
            if prices[right]>prices[left]:
                profit=prices[right]-prices[left]
                max_Profit=max(max_Profit,profit)
            else:
                left=right
            right+=1
        return max_Profit


prices = [7,1,5,3,6,4]

obj=Solution()
x=obj.maxProfit(prices)
print(x)
        
            

        
         

       
        