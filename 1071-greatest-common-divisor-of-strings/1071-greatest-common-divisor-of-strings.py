from fractions import gcd 
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1+str2!=str2+str1:
            return ""
        length=gcd(len(str1),len(str2))
        return str1[:length]
       

                







str1 = "ABCABC"
str2 = "ABC"
obj=Solution()
result=obj.gcdOfStrings(str1,str2)
print(result)