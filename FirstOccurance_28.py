class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)

x=input('Endter haystack : ')
y=input('Enter Needle : ')


obj=Solution()
result =obj.strStr(x,y)
print(result)