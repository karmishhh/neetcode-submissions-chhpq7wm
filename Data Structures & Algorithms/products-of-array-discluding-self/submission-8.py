class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefixlist = []
        prefixproduct = 1
        for i in range(len(nums)):
            prefixlist.append(prefixproduct)
            prefixproduct *= nums[i]

        postfixlist = [1] * len(nums)
        postfixproduct = 1
        for j in range(len(nums)-1, -1, -1):
            postfixlist[j] = postfixproduct
            postfixproduct *= nums[j]

        output = [1] * len(nums)

        for i in range(len(nums)):
            output[i] = prefixlist[i] * postfixlist[i]

        return output

        
        