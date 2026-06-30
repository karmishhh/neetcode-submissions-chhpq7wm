class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and ast < 0: # collision cases
                if abs(stack[-1]) > abs(ast):
                    break  # we break because the new ast has been destroyed so and there are no more collisions to check for.
                elif abs(stack[-1]) < abs(ast):
                    stack.pop()
                elif abs(stack[-1]) == abs(ast):
                    stack.pop()
                    break # we break because the new ast has been destroyed so and there are no more collisions to check for.
            # all other cases, just append
            else:
                stack.append(ast)
        return stack

                
            
        