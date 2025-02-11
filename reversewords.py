# pythonic approach with .split

class Solution:
    def reverseWords(self, s: str) -> str:
        #split the sentence into its words and store them in a list
        words = s.split()

        return " ".join(reversed(words))
#not as pythonic, uses less memory but slower overall
class Solution:
    def reverseWords(self, s: str) -> str:
        # Strip leading/trailing spaces and then split by spaces
        s = s.strip()
        start = 0
        words = []
        
        # Iterate through the string and extract words
        for i in range(len(s)):
            if s[i] == ' ':
                if start < i:  # Make sure the word length is non-zero
                    words.append(s[start:i])
                start = i + 1  # Move start pointer to the next word
        # Add the last word (if exists)
        if start < len(s):
            words.append(s[start:])
        
        # Reverse the list of words manually
        reversed_words = []
        for i in range(len(words)-1, -1, -1):
            reversed_words.append(words[i])
        
        # Join the words with a single space and return
        return ' '.join(reversed_words)