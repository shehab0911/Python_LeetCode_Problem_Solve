class Solution(object):
    def removeDuplicates(self, nums):
        j=1
        count=1
        n=len(nums)

        for i in range(1,n):
            if nums[i]==nums[i-1]:
                count+=1
            else:
                count=1
            if count <=2:
                nums[j]=nums[i]
                j+=1
        return j




nums = [1,1,1,2,2,3]
obj=Solution()
result=obj.removeDuplicates(nums)
print(result)