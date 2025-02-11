class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #get the length of the vector
        n = len(nums)
        # make an array of length n populated with 1s
        result = [1] * n

        #compute the prefix product for each index
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        #compute the suffix product and update the results vector in place
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result