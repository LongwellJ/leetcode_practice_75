class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #start pointer for the zeros
        left = 0
        #iterate through the nums with the right pointer
        for right in range(len(nums)):
            #Check if the right index is equal to 0
            if nums[right] != 0:
                #if it is not equal to zero, exchange the left and right pointers
                nums[right], nums[left] = nums[left], nums[right]
                # move the left pointer over one
                left += 1
            #no matter if right is 0 or not, move it over one
            right += 1
