class Solution(object):
    def subarraySum(self, nums, k):
        prefix = {0: 1}
        curr_sum = 0
        res = 0

        for num in nums:
            curr_sum += num

            if curr_sum - k in prefix:
                res += prefix[curr_sum - k]

            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1

        return res
        