class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairlist = [(p,s) for p,s in zip(position,speed)]
        pairlist.sort(reverse=True)
        stack = []
        for p,s in pairlist:
            time_to_the_end = (target - p)/s

            if not stack or time_to_the_end > stack[-1]:
                stack.append(time_to_the_end)
        
        return len(stack)
        