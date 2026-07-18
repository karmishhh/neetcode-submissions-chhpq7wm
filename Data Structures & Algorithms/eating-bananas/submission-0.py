class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            rate = (left + right) // 2 # find the mid rate 
            hrs_required = 0
            for p in piles:
                hrs_required += math.ceil(float(p)/rate)
            if hrs_required > h:
                left = rate + 1
            elif hrs_required < h:
                right = rate - 1
                res = rate
            else:
                right = rate - 1 # or left = rate + 1
                res = rate
        return res
                


        