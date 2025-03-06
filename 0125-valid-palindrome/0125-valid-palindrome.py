
class Solution(object):
    def isPalindrome(self, s):
        left=0
        right = len(s)-1
        while left<right:
            if not s[left].isalnum():
                left+=1
            elif not s[right].isalnum():
                right-=1
            elif s[left].lower()==s[right].lower():
                left+=1
                right-=1
            else:
                return False
        
        return True

        


s1="race a car"
s = "A man, a plan, a canal: Panama"
obj=Solution()
x=obj.isPalindrome(s)
print(x)