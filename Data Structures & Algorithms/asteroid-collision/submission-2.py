class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0: # collision cases
                if abs(stack[-1]) > abs(ast):
                    break
                elif abs(stack[-1]) < abs(ast):
                    stack.pop()
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break
            # all other cases, just append
            else:
                stack.append(ast)
        return stack

                
            
        