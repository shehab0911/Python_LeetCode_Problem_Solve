class Solution(object):
    def decodeString(self, s):
        stack = []
        current_string = ""
        current_number = 0
    
        for char in s:
            if char.isdigit():  
                current_number = current_number * 10 + int(char)
            elif char == '[':  
                stack.append((current_string, current_number))
                current_string = ""
                current_number = 0
            elif char == ']':  
                last_string, num = stack.pop()
                current_string = last_string + num * current_string
            else:  
                current_string += char
    
        return current_string
        
    

       
        