from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        r = Counter(ransomNote)
        m = Counter(magazine)

        for char, count in r.items():
            if m[char] < count:
                return False
        return True
       
       
        