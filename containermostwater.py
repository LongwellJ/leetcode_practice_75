class Solution:
    def maxArea(self, height: List[int]) -> int:
        # make two pointers, one for the index of the left and one for the index of the right
        left = 0
        right = len(height) - 1
        maximum = 0

        #iterate through the array as long as right and left are not touching/overlap

        while left < right:
            #current height is the min between the right and left height
            current_height = min(height[left], height[right])
            #current width of the box is right - left index
            current_width = right - left
            # now find current area with height * width 
            current_area = current_height * current_width
            #Update max area if we have found larger current area
            maximum = max(maximum, current_area)

            #update the pointers. check if the right or left height is smaller
            if height[left] < height[right]:
                left += 1
            else:
                right -=1
        #once the while loop is done, we have overlap of left and right
        return maximum