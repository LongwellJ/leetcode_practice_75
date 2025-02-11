#Given an array of integers nums and an integer target, return the indices of the two numbers that add up to the target.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#brute force

def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
            
nums = [2,7,11,15]
target = 9
print(twosum(nums, target))



class solution(object):
    def twosum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

nums = [2,7,11,15]
target = 9
s = solution()
print(s.twosum(nums, target))


#two pass hash table

def twosum(nums, target):
    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = i
        
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dic and dic[complement] != i:
            return [i, dic[complement]]
    return []




nums = [2,7,11,15]
target = 9
print(twosum(nums, target))


#one pass hash table

def twosum(nums, target):
    dic = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dic:
            return [dic[complement], i]
        dic[nums[i]] = i
    return []

nums = [2,7,11,15]
target = 9
print(twosum(nums, target))
