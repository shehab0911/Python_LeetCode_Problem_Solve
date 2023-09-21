import statistics
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array = nums1 + nums2
        array.sort()

        mid = len(array)

        if mid % 2 == 0:
            x = array[mid // 2] + array[mid // 2 - 1]
            return x / 2.0
        else:
            n = array[mid // 2]
            return float(n)

num1 = [1, 2, 7]
nums2 = [3, 4]

obj = Solution()
result = obj.findMedianSortedArrays(num1, nums2)
print(result)

