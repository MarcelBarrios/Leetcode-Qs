# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str

        The strategy is to add the two binary strings from right to left, just like you would add decimal 
        numbers on paper. We need to keep track of a carry value as we go.
        """
        # We'll start with a carry of 0 and an empty result string. We'll also use two pointers, i and j, 
        # to track our position in strings a and b, starting from the very end of each.
        result = ""
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        # We'll continue looping as long as we have digits to process in either string (i or j is still valid)
        # or if there is a remaining carry from a previous addition.
        # O(n + m)
        while i >= 0 or j >= 0 or carry:
            # Start the sum for the current column with the carry from the previous column.
            # If there was no carry, this starts at 0.
            total_sum = carry
            
            # If there are still digits left in string 'a', add the current digit to the sum.
            if i >= 0:
                # Convert the character ('0' or '1') to an integer (0 or 1) before adding.
                total_sum += int(a[i])
                # Move the pointer for 'a' one step to the left for the next iteration.
                i -= 1
            
            # If there are still digits left in string 'b', add the current digit to the sum.
            if j >= 0:
                # Convert the character to an integer before adding.
                total_sum += int(b[j])
                # Move the pointer for 'b' one step to the left for the next iteration.
                j -= 1
            
            # Append the binary result of this column to our result string.
            # `total_sum % 2` gives the remainder, which is the binary digit for this position.
            # (e.g., 0%2=0, 1%2=1, 2%2=0, 3%2=1). We prepend it because we're building the string from right to left.
            result = str(total_sum % 2) + result

            # Calculate the carry for the next column to the left.
            # `total_sum // 2` uses integer division. If the sum was 0 or 1, the carry is 0.
            # If the sum was 2 or 3, the carry is 1.
            carry = total_sum // 2
            
        # Once the loop is finished, return the final constructed binary string.
        return result
    # O(n+m)