class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # define first and second, make sure they are as high as can be
        first, second = float('inf'), float('inf')
        #iterate through the nums vector
        for num in nums:
            #if num is less than or equal to the first, then it becomes the new first
            if num <= first:
                first = num
            #if it is not less than or equal to the first, check if its less than or equal to the second
            elif num <= second:
                second = num
            # if its more than the first and second, then its the third, and we have a sequence that fits, so return true
            else:
                return True
        #after iterating through each num in the vector, if we still haven't returned, then there is no sequence that fits, so return false
        return False