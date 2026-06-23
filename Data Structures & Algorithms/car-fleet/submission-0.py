class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairlist = [(p,s) for p,s in zip(position,speed)]
        pairlist.sort(reverse=True)
        print(pairlist)
        stack = []
        for valset in pairlist:
            p,s = valset
            distance_left = target - p
            time_to_the_end = (distance_left/s)

            if not stack or time_to_the_end > stack[-1]:
                stack.append(time_to_the_end)
        
        return len(stack)
        