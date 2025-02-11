class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        
        #make a dict of the vowels
        vowels = {'a', 'e', 'i', 'o', 'u'}
        #create two vars, max_count and count, initiate as the same thing
        #initiated as the sum of the vowels in s within range k
        max_count = count = sum(1 for i in range(k) if s[i] in vowels)

        # iterate through k to s
        for i in range(k, len(s)):
            #we add the new vowels and subtract the old ones that are no longer in the sliding window
            count += (s[i] in vowels) - (s[i-k] in vowels)
            # update max count to be the larger of the old one and the new one
            max_count = max(max_count, count)

        return max_count