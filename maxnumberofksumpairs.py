class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_counts = {}  # Use a dictionary to store the counts of each number

        for num in nums:
            complement = k - num
            if complement in num_counts and num_counts[complement] > 0:
                count += 1
                num_counts[complement] -= 1  # Decrement count after using it
            else:
                if num not in num_counts:
                    num_counts[num] = 0
                num_counts[num] += 1  # Increment the number's count

        return count