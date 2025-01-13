class Solution(object):
    def mergeAlternately(self, word1, word2):
        list1 = []
        i = j = 0
        p = len(word1)
        q = len(word2)
        
        # Alternate between characters of word1 and word2
        while i < p or j < q:
            if i < p:  # Add from word1 if there are remaining characters
                list1.append(word1[i])
                i += 1
            if j < q:  # Add from word2 if there are remaining characters
                list1.append(word2[j])
                j += 1
        
        return ''.join(list1)  # Convert list to a string

# Test the function
word1 = "abc"
word2 = "pqr"
obj = Solution()
result = obj.mergeAlternately(word1, word2)
print(result)
