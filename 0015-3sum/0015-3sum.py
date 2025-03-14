class Solution(object):
    def threeSum(self, nums):
        target=0
        nums.sort()
        s=set()
        output=[]


        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            while j<k:
                sum=nums[i]+nums[j]+nums[k]
                if sum==target:
                    s.add((nums[i],nums[j],nums[k]))
                    
                    j+=1
                    k-=1

                elif sum>0:
                    k-=1
                else:
                    j+=1
        #output=list(s)
        for l in s:
            output.append(list(l))

        return output

nums = [-1, 0, 1, 2, -1, -4]
obj=Solution()
result=obj.threeSum(nums)
print(result)