class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s)==sorted(t)


s = "a"
t = "ab"
obj=Solution()
result=obj.isAnagram(s,t)
print(result)