class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char not in '+-*/':
                stack.append(int(char))
            else:
                if stack:
                    num1 = stack.pop() # top value
                    num2 = stack.pop() # 2nd value
                    if char == '+':
                        stack.append(num2+num1)
                    elif char == '-':
                        stack.append(num2-num1) # we can't do num1-num2 since it violates the order of elements in the question stem! 
                    elif char == '*':
                        stack.append(num2*num1)
                    else:
                        stack.append(int(num2 / num1))
        return stack[-1]
                    