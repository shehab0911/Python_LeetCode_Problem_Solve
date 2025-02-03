class Solution(object):
    def shuffle(self, nums, n):
        list1=[]
        
    
        for x in range(len(nums)-n):
            j=n+x
            list1.append(nums[x])
            list1.append(nums[j])
        return list1


        