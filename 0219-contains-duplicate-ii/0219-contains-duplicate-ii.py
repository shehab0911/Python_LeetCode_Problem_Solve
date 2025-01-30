from collections import Counter
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        list1=[]
        n=Counter(nums)
        for keys ,values in n.items():
            if values ==1:
                list1.append(keys)
        if len(list1)<=0:
            return False
        elif len(list1)==1:
            return False
        else:
            return True

        
        
        