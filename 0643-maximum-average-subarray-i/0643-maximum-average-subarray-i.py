class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum=0
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        t=round(max_sum / k,5)
        return t
        