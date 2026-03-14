class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        count = 0
        length = len(flowerbed)

        for i in range(length):

            if flowerbed[i] == 0:

                prev = 0 if i == 0 else flowerbed[i-1]
                next = 0 if i == length-1 else flowerbed[i+1]

                if prev == 0 and next == 0:
                    flowerbed[i] = 1
                    count += 1

        if n <= count:
            return True
        return False


flowerbed = [0,0,1,0,1]
n = 1

obj = Solution()
result = obj.canPlaceFlowers(flowerbed, n)
print(result)