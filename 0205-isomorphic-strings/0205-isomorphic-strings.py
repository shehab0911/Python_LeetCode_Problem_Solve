class Solution(object):
    def isIsomorphic(self, s, t):
        s1=set(s)
        t1=set(t)
        if len(s1)==len(t1) == len(zip(s,t)):
            return True
        else:
            return False
        