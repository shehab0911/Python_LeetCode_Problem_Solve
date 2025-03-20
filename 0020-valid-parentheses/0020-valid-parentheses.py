class Solution(object):
    def isValid(self, s):
        hasmap={")":"(","}":"{","]":"["}
        stack=[]
        
        for c in s:
            if c not in hasmap:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped=stack.pop()
                    if popped!=hasmap[c]:
                        return False
        return not stack
       
        