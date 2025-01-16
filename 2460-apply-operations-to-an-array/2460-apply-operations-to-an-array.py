class Solution(object):
    def applyOperations(self, nums):
        n = len(nums)
        i=0
        j = 1
        k=1
        while i<n and j<n:
            if nums[i]==nums[j]:
                nums[i]=nums[i]+nums[j]
                nums[j] = 0
                i+=1
                j+=1
            else:
                i+=1
                j+=1

        list2=[]
        list1=[]
        for i in nums:
            if i!=0:
                list2.append(i)
            else:
                list1.append(i)


        return list2+list1









nums = [1,2,2,1,1,0]

obj=Solution()
result=obj.applyOperations(nums)
print(result)

