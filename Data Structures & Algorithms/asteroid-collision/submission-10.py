class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        # we 'break' because the new ast has been destroyed so and there are no more collisions to check for.
        for ast in asteroids:
            alive = True
            while stack and stack[-1] > 0 and ast < 0:
                if abs(stack[-1]) > abs(ast):
                    alive = False # the incoming ast is destroyed
                    break
                elif abs(stack[-1]) < abs(ast):
                    stack.pop() # the incoming ast destroyed the top of stack element
                else: # both equal ~ top of stack removed and incoming ast also destroyed 
                    stack.pop()
                    alive = False
                    break
            
            if alive: # if ast hasn't been destroyed yet we add it to stack since it represents all other cases (both same direction or both opposite direction - moving away from each other and not towards each other)
                stack.append(ast)
        return stack
        