from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        dict=defaultdict(list)
        for i in strs:
            word="".join(sorted(i))
            dict[word].append(i)
        return list(dict.values())









strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
obj=Solution()
result=obj.groupAnagrams(strs)
print(result)
#[["bat"],["nat","tan"],["ate","eat","tea"]]
