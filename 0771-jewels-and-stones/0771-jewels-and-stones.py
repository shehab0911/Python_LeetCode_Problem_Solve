from collections import Counter
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        
        count_2=Counter(stones)
        return sum(count_2[j] for j in jewels)
        
        
        