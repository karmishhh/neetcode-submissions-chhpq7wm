class Solution:
    def isValid(self, s: str) -> bool: # e.g., "([{}])"
        if len(s) > 1:
            stack = []
            opening_brackets = ['(','{','[']
            mapping = {')':'(',
                        '}':'{',
                        ']':'['    
                            }
            for char in s:
                if char in opening_brackets: # means an opening bracket so append it to the stack
                    stack.append(char)
                else: # means closing bracket
                    target_closing_bracket = mapping.get(char)
                    if stack:
                        if target_closing_bracket != stack.pop():
                            return False
                    else:
                        return False
            
            if len(stack) != 0:
                return False
            else:
                return True
        else:
            return False



        