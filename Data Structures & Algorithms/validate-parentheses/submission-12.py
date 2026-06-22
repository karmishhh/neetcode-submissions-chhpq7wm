class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(',
                        '}':'{',
                        ']':'['    
                            }
        for char in s:
            if char in mapping: # closing bracket
                if not stack or stack.pop() != mapping.get(char):
                    return False
            else: # opening bracket
                stack.append(char)

        if stack:
            return False
        return True      
        
        