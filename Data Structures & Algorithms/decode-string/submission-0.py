class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        # "2[a3[b]]c"
        for char in s:
            if char != ']':
                stack.append(char) # ['2','[','a','3','[','b']
            else:
                current = ''
                while stack and stack[-1] != '[':
                    current = stack.pop() + current # ['2','[','a','3','['] - current becomes b
                    print(current)
                stack.pop() # remove the opening bracket [ - # ['2','[','a','3']
                num = ''
                while stack and stack[-1].isdigit(): # get the numbers - 
                    num = stack.pop() + num # ['2','[','a']  num becomes '3'
                # append the calculation now to stack
                stack.append(current * int(num))
        return ''.join(stack)
            


                    
        