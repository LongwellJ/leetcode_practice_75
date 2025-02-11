class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        #find the highest number of candies in the array
        max_candies = max(candies)
        #Return the array of trues and falses
        return [candy + extraCandies >= max_candies for candy in candies]