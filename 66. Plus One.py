# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]

        The key is to work from right to left, just like you would when adding one to a number on paper.
        """
        # Gets the number of elements in the list.
        n = len(digits)
        
        # This starts a for loop that iterates backward.
        for i in range(n - 1, -1, -1):
            # check if digits[i] is 9
            if digits[i] < 9:
                # add 1 to i
                digits[i] += 1
                # return list
                return digits
            
            else:
                # Since the digit was 9, it becomes 0.
                digits[i] = 0
        
        # This line is only reached if the entire loop finished (meaning all digits were 9). 
        # It creates a new list by placing a 1 at the front of our list of zeros.
        return [1] + digits