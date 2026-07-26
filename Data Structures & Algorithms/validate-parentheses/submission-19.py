class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char not in hashmap:
                stack.append(char)
            else:
                opening = hashmap.get(char)
                if stack and opening == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

        