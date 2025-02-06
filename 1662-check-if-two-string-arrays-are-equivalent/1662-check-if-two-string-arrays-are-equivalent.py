class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        x="".join(word1)
        y="".join(word2)
        if x==y:
            return True
        else:
            return False
       
        