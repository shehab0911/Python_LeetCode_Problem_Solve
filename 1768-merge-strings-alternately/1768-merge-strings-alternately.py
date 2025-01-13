class Solution(object):
    def mergeAlternately(self, word1, word2):
        list1 = []
        i = j = 0
        p = len(word1)
        q = len(word2)
        
         
        while i < p or j < q:
            if i < p:  
                list1.append(word1[i])
                i += 1
            if j < q: 
                list1.append(word2[j])
                j += 1
        
        return ''.join(list1) 


word1 = "abc"
word2 = "pqr"
obj = Solution()
result = obj.mergeAlternately(word1, word2)
print(result)
