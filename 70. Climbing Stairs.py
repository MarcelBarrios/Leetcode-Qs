# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Handle the base cases for the first two steps.
        if n <= 2:
            return n
        
        # Initialize pointers for the two preceding steps.
        # To calculate step 3, we need ways(2) and ways(1).
        one_step_back = 2  # Represents ways to climb n-1 stairs
        two_steps_back = 1 # Represents ways to climb n-2 stairs
        
        # Iterate from the 3rd step up to the n-th step.
        for _ in range(3, n + 1):
            # The number of ways to reach the current step is the sum of the ways to reach the previous two.
            current_ways = one_step_back + two_steps_back
            
            # Update the pointers for the next iteration.
            # The previous one_step_back becomes the new two_steps_back.
            two_steps_back = one_step_back
            # The current number of ways becomes the new one_step_back.
            one_step_back = current_ways
            
        # The final answer is the number of ways to reach the n-th step.
        return one_step_back
    # O(n)