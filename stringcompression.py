class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0  # Pointer to write the compressed characters
        read_index = 0  # Pointer to read through the input list
        n = len(chars)
        #iterate through the list of characters with a while loop
        while read_index < n:
            #get the individual char in positon read_index
            char = chars[read_index]
            #set the char counter to 0 
            count = 0
            
            # Count how many times the current character repeats
            while read_index < n and chars[read_index] == char:
                read_index += 1
                count += 1
            
            # Write the character itself in the write_index and add one to the write_index pointer
            chars[write_index] = char
            write_index += 1
            
            # If there is more than 1 of the character in a row, then count is greater than 1. So write the count as a string
            if count > 1:
                for digit in str(count):
                    chars[write_index] = digit
                    write_index += 1
        
        # Return the new length of the compressed string
        return write_index