class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for char in operations:
            if char not in '+CD':
                stack.append(int(char))
            elif char == '+':
                    stack.append(stack[-1] + stack[-2])
            elif char == 'C':
                    stack.pop()
            elif char =='D':
                    stack.append(2*stack[-1])
        return sum(stack)
        