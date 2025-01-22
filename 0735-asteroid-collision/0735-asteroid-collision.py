class Solution(object):
    def asteroidCollision(self, asteroids):
        stack=[]
        for x in asteroids:
            while stack and x<0 and stack[-1]>0:
                if abs(x)>stack[-1]:
                    stack.pop()
                elif abs(x)==stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(x)
        return stack

        
        