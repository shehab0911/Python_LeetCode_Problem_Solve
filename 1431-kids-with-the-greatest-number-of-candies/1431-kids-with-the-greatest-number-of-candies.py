class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        result=max(candies)
        list1=[]
        for x in candies:
            sum=x+extraCandies
            if sum>=result:
                list1.append(True)
            else:
                list1.append(False)

        return list1

        
        