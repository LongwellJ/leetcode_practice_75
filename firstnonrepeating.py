#input s

s = 'The quick brown fox jumps over the lazy dog.'
s1 = "leetcode"
s2 = "loveleetcode"
s3 = "aabb"
#brute force
#find first non repeating character in a string and return the index. If there is no such character that does not repeat, then we will return -1

def first_non_repeating(s:str):
    #Get the length of the string
    length = len(s)
    #iterate through the string
    for i in range(len(s)):
        #return the index if it is not in rest of the string
        if s[i] not in s[i+1:] and s[i] not in s[:i]:
            return i
    return -1
    

print(first_non_repeating(s))
print(first_non_repeating(s1))
print(first_non_repeating(s2))
print(first_non_repeating(s3))

# two pass hash table

def first_non_repeating(s:str):
    #create a dict
    dic = {}
    #iterate through the string
    for i in range(len(s)):
        #if the character is not in the dict then add it
        if s[i] not in dic:
            dic[s[i]] = i
        else:
            dic[s[i]] = -1
    #iterate through the dict and return the index of the first non repeating character AKA the first key that has a value that is not -1
    for i in dic:
        if dic[i] != -1:
            return dic[i]
    return -1

print(first_non_repeating(s))
print(first_non_repeating(s1))
print(first_non_repeating(s2))
print(first_non_repeating(s3))

# BEST ONE
#using the Counter function from collections for hashable objects like strings
def first_non_repeating(s:str):

    from collections import Counter
    #count the character frequencies
    char_count = Counter(s)
    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i
    return - 1



print(first_non_repeating(s))
print(first_non_repeating(s1))
print(first_non_repeating(s2))
print(first_non_repeating(s3))

#one pass hash table with an ordered dict and a set
def first_non_repeating(s:str):
    #import the ordered dict package from collections
    from collections import OrderedDict
    #create an ordered dict
    dic = OrderedDict()
    seen = set()
    #iterate through the input string
    for i, char in enumerate(s):
        #check if the character has been seen before by checking if its in the seen set
        if char in seen:
            #if its in the seen set, then it previously got added to the dic at some point. Check if it is still there
            if char in dic:
                #since its still here, now we'll delete it
                del dic[char]
            #If its not there anymore, just move onto the next index in the string
        #If the character is not in the seen set
        else:
            #Then we add it to the dict that we'll return, if the char is seen again it will be deleted from the dict
            dic[char] = i 
            #Then we add it to the seen set since we just checked and it has never been seen before
            seen.add(char)

    return next(iter(dic.values()), -1) #retun the first index in the ordered dic, since if it was seen again it would have been deleted. If it is empty and does not have values that are iterable, then return -1


print(first_non_repeating(s))
print(first_non_repeating(s1))
print(first_non_repeating(s2))
print(first_non_repeating(s3))