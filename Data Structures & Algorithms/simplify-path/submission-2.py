class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        word = ''
        for s in path + "/":
            if s == '/':
                if word == '..': # what we have built until now
                    if stack:
                        stack.pop()
                
                elif word != '.' and word != '':
                    stack.append(word)
                
                word = '' # reset the word after appending to stack
            else:
                word += s

        
        return '/' + "/".join(stack)

        