class Solution(object):
    def findWordsContaining(self, words, x):
        list1=[]
        for i in range(len(words)):
            if x in words[i]:
                list1.append(i)
        return list1
       
        