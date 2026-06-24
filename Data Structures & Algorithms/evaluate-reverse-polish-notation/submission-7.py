class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for idx, val in enumerate(tokens):
                if val in ['+','-','*','/']:
                    a = int(tokens[idx-2])
                    b = int(tokens[idx-1])
                    if val == '+':
                        result = a+b
                    elif val == '-':
                        result = a-b
                    elif val == '*':
                        result = a*b
                    else:
                        result = int(a/b)
                    
                    tokens = tokens[:idx-2] + [str(result)] + tokens[idx+1:]
                    break
        return int(tokens[0])

                

                
        