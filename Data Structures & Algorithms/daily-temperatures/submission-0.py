class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            pointer = idx + 1
            while pointer < len(temperatures):
                if temperatures[pointer] > temp:
                    res[idx] = pointer - idx
                    break
                else:
                    pointer += 1
        return res

            
                



# make an answer array, all zeros (0 is the default "never found")
# for each day i:
#     for each later day j (starting at i+1):
#         if day j is warmer than day i:
#             record j - i into answer[i]
#             stop scanning (break) — we want the FIRST warmer day
# return answer