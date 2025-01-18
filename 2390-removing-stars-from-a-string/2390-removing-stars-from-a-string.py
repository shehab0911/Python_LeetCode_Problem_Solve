class Solution(object):
    def removeStars(self, s):
        list1=[]
        for i in s:
            if i!='*':
                list1.append(i)
            elif i=='*':
                list1.pop()
        return "".join(list1)




s = "leet**cod*e"
obj=Solution()
result=obj.removeStars(s)
print(result)