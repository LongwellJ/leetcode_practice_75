class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #make two pointers for s and for t
        i = 0
        j = 0
        
        #check if i and j are still less than the lengths of s and t
        while i < len(s) and j < len(t):
            #check if the character of s is the same as the character of t
            if s[i] == t[j]:
                #if it is, increase i by one to show we have a letter from s in t
                i += 1
            # increase j no matter what to move onto the next letter in j
            j += 1
        #Once we have iterated all the way through either s or j, return true or flase depedning on if i == len(s) which would mean that we have seen all the letters of s in order inside of t
        return i == len(s)
    


def is_subsequence_many_s(s, t_index_map):
    """Checks if s is a subsequence of t using the preprocessed index map."""
    prev_index = -1
    for char in s:
        if char not in t_index_map:
            return False  # Character not found in t

        indices = t_index_map[char]
        
        #Efficiently find the next greater index using binary search
        low = 0
        high = len(indices) - 1
        next_index = -1

        while low <= high:
            mid = (low + high) // 2
            if indices[mid] > prev_index:
                next_index = indices[mid]
                high = mid - 1 #Try to find an even smaller index
            else:
                low = mid + 1
        
        if next_index == -1:
            return False

        prev_index = next_index
    return True

def preprocess_t(t):
    """Creates an index map for t."""
    t_index_map = {}
    for i, char in enumerate(t):
        if char not in t_index_map:
            t_index_map[char] = []
        t_index_map[char].append(i)
    return t_index_map


# Example Usage with Preprocessing:
t = "ahbgdc"
t_index_map = preprocess_t(t)

print(is_subsequence_many_s("abc", t_index_map))  # Output: True
print(is_subsequence_many_s("axc", t_index_map))  # Output: False
print(is_subsequence_many_s("ac", t_index_map)) # Output: True

# Now you can efficiently check many different 's' strings against the same 't'
# without repeatedly scanning 't'.  Just preprocess 't' once.