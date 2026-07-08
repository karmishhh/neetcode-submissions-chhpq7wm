class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        listt = path.split('/')
        for s in listt:
            if s == '..':
                if stack:
                    stack.pop()
            elif s != '.' and s != '':
                stack.append(s)
        
        return "/" + '/'.join(stack)
        