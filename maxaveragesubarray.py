class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        #if we are given a k which is longer than the length of the nums array, then return 0
        if len(nums) < k:
            return 0
        
        #calcualte the sum of the first k elements

        current_sum = sum(nums[:k])
        #calculate the first max_average
        max_average = current_sum / k

        #iterate through the nums
        #[1,2,3,4,5,6,7], k =4
        for i in range(1, len(nums) - k + 1):
            #get the current sum based on where the pointer index is
            current_sum = current_sum - nums[i-1] + nums[i+k-1]
            #update current average by dividing by k
            current_average = current_sum / k
            #update the max_average if the current one is bigger
            max_average = max(max_average, current_average)

        return max_average