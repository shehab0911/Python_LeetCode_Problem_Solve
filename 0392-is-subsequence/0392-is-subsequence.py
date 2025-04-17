class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        j=0
        while j<len(t):
            if i<len(s) and s[i]==t[j]:
                i+=1
            j+=1
        return i == len(s)
                
        
