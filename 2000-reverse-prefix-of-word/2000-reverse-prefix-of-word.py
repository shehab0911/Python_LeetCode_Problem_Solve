class Solution(object):
    def reversePrefix(self, word, ch):
        x=word.find(ch)
        word1=list(word)
        y=word1[:x+1]
        z=word1[x+1:]
        res=y[::-1]+z
        return "".join(res)



word = "abcdefd"
ch = "d"
obj=Solution()
result=obj.reversePrefix(word,ch)
print(result)