class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        word = ''
        for s in path + "/":
            if s == '/':
                if word == '..':
                    if stack:
                        stack.pop()
                
                elif word != '.' and word != '':
                    stack.append(word)
                
                word = ''
            else:
                word += s

        
        return '/' + "/".join(stack)

        