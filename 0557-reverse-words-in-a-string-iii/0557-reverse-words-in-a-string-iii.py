class Solution(object):
    def reverseWords(self, s):
        list1=[]
        for i in s.split():
            list1.append(i[::-1])
        return " ".join(list1)

    
        