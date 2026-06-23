class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # we will store a tuple of index and temp
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_idx, stack_val = stack.pop()
                res[stack_idx] = idx - stack_idx
            stack.append((idx, temp)) # we are doing this - Because every day, without exception, needs to go on the stack to wait for its own warmer day — and you don't know yet when (or if) that warmer day will arrive, so the only thing you can do right now is park it and move on.
        return res

# The while loop answers: "does the current day temp resolve anyone who's still waiting?" It pops everyone on the stack who's been waiting for a warmer day and just found it (current temp is warmer than theirs). Those days are now done — answer recorded, gone from the stack forever.
#The append answers a different question: "the current day itself — has it found its warmer day yet?" And the answer is always no, not yet. The current day can resolve earlier days (that's the while), but nothing has come after it yet to resolve it. It hasn't seen its own future. So it has to get in line and wait, exactly like every day before it did. That's why it's unconditional — being unresolved is the default state of a day the moment you arrive at it.
#Here's the key insight that makes the "regardless" click: the pop and the append are about different days. The while pops other, earlier days that the current day resolves. The append adds the current day to wait. The current day is never resolved by itself — it can only ever be resolved by some later day, which hasn't been processed yet. So at the moment you're standing on day idx, there is genuinely nothing that could resolve it, and parking it is the only correct move.
#Trace it on [73, 74, 75] to feel it:
#idx=0, temp=73: stack empty, while doesn't run. append → stack=[(0,73)]
#idx=1, temp=74: 73<74 → pop (0,73), res[0]=1-0=1. append → stack=[(1,74)]
#idx=2, temp=75: 74<75 → pop (1,74), res[1]=2-1=1. append → stack=[(2,75)]
#end. res=[1,1,0]