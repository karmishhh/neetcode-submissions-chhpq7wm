class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val in '+-*/':
                b = int(stack.pop()) # top values
                a = int(stack.pop()) # second top values
                if val == '+':
                    result = a+b
                elif val == '-':
                    result = a-b
                elif val == '*':
                    result = a*b
                else:
                    result = int(a/b)
                stack.append(result)
            else:
                stack.append(val)
        return int(stack[0])
