class Solution(object):
    def largestAltitude(self, gain):
        left=0
        list1=[]
        ssum=0
        for i in gain:
            ssum=ssum+i
            list1.append(ssum)
        val=max(list1)
        if val<0:
            return 0
        else:
            return val


        
        