class Solution:
    def mySqrt(self, x: int) -> int:
        # brute force
        if x==0 or x==1:
            return x
            
        res = 0
        for i in range(x):
            if i*i <= x:
                res = i
            else:
                break
        return res        