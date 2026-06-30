class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
                continue
            while stack and stack[-1] > 0 and ast < 0 and (abs(ast) > stack[-1]): # chain reaction
                stack.pop()

            if not stack:
                stack.append(ast)
            
            elif stack[-1] > 0 and ast < 0 and (abs(ast) == stack[-1]):
                stack.pop() # mutual destruction

            elif (ast > 0 and stack[-1] > 0) or (ast < 0 and stack[-1] < 0):
                stack.append(ast)

            elif stack[-1] > 0 and ast < 0 and (abs(ast) < stack[-1]):
                # do nothing here
                pass
            elif stack[-1] < 0 and ast > 0:
                stack.append(ast)
        
        return stack


        