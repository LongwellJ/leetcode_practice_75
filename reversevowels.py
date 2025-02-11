class Solution:
    def reverseVowels(self, s: str) -> str:
        #Make a set of the vowels and include capitals
        vowels = set('aeiouAEIOU')
        #convert the string to a list so it is mutable
        s = list(s)
        left, right = 0, len(s)-1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -=1

            s[left], s[right] = s[right], s[left]
        
            #move both pointers closer together

            left += 1
            right -= 1
        #convert the list back into a string
        return "".join(s)
        