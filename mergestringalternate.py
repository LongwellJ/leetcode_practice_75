#Low memory but high runtime solution with zip_longest

from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join(a+b if b else a for a, b in zip_longest(word1, word2, fillvalue=""))
    

#average memory and average speed

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        #make an array to hold the merged data
        merged = []
        #Make a pointer starting at 0 for both variables
        i,j = 0,0
        #Get the lengths of both words
        len1, len2, = len(word1), len(word2)
        #iterate over i and j until the length is done
        while i < len1 and j < len2:
            merged.append(word1[i])
            merged.append(word2[j])
            i +=1
            j +=1

        if len1 < len2:
            merged.append(word2[i:])
        if len2 < len1:
            merged.append(word1[j:])

        return "".join(merged)
