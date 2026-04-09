class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            if i == 0:
                suffix_set = nums[i+1:]
                print(suffix_set)
                product = 1
                for val in suffix_set:
                    product *= val
                output.append(product)
            else:
                prefix_set = nums[:i]
                suffix_set = nums[i+1:]
                print(nums[i], prefix_set, suffix_set)
                product = 1
                for val in prefix_set:
                    product*=val
                for val in suffix_set:
                    product *= val
                output.append(product)
        return output
