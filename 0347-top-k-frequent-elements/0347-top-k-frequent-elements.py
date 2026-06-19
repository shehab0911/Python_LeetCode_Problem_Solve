from collections import Counter

class Solution(object):
    def topKFrequent(self, nums, k):
       count = Counter(nums)
       return [num for num, freq in count.most_common(k)]