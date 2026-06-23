class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # we will store a tuple of index and temp
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                stack_idx, stack_val = stack.pop()
                res[stack_idx] = idx - stack_idx
            stack.append([idx, temp])
        return res

        