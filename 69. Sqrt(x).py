# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

# Constraints:

# 0 <= x <= 231 - 1

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        The algorithm uses binary search to quickly find the answer within the range of numbers from 1 to x. 
        It repeatedly checks the middle number, discarding half of the search space until it finds the 
        largest integer whose square is not greater than the target.
        """
        # Handle the base case for 0.
        if x == 0:
            return 0
        
        # Initialize the search space for binary search.
        left, right = 1, x
        # Initialize a variable to store the potential result.
        result = 0
        
        # Perform binary search until the left and right pointers cross.
        # O(log n)
        while left <= right:
            # Calculate the middle point to avoid potential overflow.
            mid = left + (right - left) // 2
            
            # If the square of mid is greater than x, mid is too large.
            if mid * mid > x:
                # Discard the right half of the search space.
                right = mid - 1
            # If the square of mid is less than or equal to x, mid is a candidate.
            else:
                # Store this candidate as it's the best one we've found so far.
                result = mid
                # Try to find a larger candidate in the right half.
                left = mid + 1
                
        # Return the last valid candidate found.
        return result
    
    # O(log n)