class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []        
        pre = 1
        prefix = []
        for val in nums:
            pre *= val
            prefix.append(pre)
        
        post = 1
        postfix = []
        for val in nums[::-1]:
            post*= val
            postfix.append(post)
        postfix = postfix[::-1]

        for i in range(len(nums)):
            pre = prefix[i-1] if i > 0 else 1
            post = postfix[i+1] if i <len(nums) -1 else 1
            output.append(pre*post)
        return output

        