class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for val in operations:
            if val not in '+CD':
                stack.append(int(val))
            elif val == '+':
                stack.append(stack[-1] + stack[-2])
            elif val == 'D':
                stack.append(stack[-1]*2)
            elif val =='C':
                stack.pop()
        return sum(stack)
        