class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        #Keep count of how many flowers we can add
        count = 0
        length = len(flowerbed)
        #iterate over the length of the flower bed
        for i in range(length):
            #Check if the index has no flower
            if flowerbed[i] == 0:
                #Check if it has the right and left empty. make sure to handle edges
                empty_left = (i==0) or (flowerbed[i-1] == 0)
                empty_right = (length - i == 1) or (flowerbed[i + 1] == 0)
                #Check if the results of the above are 1 and 1
                if empty_left and empty_right:
                    #If they are, we can plant a flower, so add one to count and change the number in the flowerbed array to 1
                    count += 1
                    flowerbed[i] = 1
                    # if we can stop early, then do so
                    if count >= n:
                        return True
        # if we are done but did not stop early, check if we can plant as many or more than n flowers
        return count >= n