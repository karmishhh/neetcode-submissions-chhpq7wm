class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}
        stack = []
        if len(s) == 1:
            return False
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                opening = hashmap.get(char)
                if stack and opening == stack[-1]:
                    stack.pop()
                    continue
                else:
                    return False
        if stack:
            return False
        return True

        