class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        
        l = 0
        r = len(height) - 1
        leftmax = height[l]
        rightmax = height[r]
        result = 0
        
        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, height[l])
                result += leftmax - height[l]
            else:
                r -= 1
                rightmax = max(rightmax, height[r])  
                result += rightmax - height[r]
        
        return result
        

       

        