#Great runtime and low memory usage

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
         # Check if str1 and str2 have a common pattern
        if str1 + str2 != str2 + str1:
            return ""

        # Find the GCD of the lengths of str1 and str2
        gcd_length = gcd(len(str1), len(str2))
        
        # The GCD string is the prefix of str1 with length gcd_length
        return str2[:gcd_length]

         
        