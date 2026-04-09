class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return False

        stack = []
        mapping = {'}': '{', ')': '(', ']': '['}
        
        for i in range(len(s)):
            
            if s[i] == '(' or s[i] == '{' or s[i] =='[':
                stack.append(s[i])
            elif s[i] not in mapping:
                return False
            else:
                if stack:
                    mapping_found = mapping.get(s[i])
                    if mapping_found != stack.pop():
                        return False
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
                    