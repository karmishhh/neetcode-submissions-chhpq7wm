class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefixproduct = 1
        for i in range(len(nums)):
            output[i] = prefixproduct
            prefixproduct *= nums[i]
        postfixproduct = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfixproduct
            postfixproduct *= nums[i]
        
        return output