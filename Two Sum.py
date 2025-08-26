# Given an array of integers nums and an integer target, return indices of the two 
# numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use
#  the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        as you loop through the array, for each number, you calculate the "complement" you would need 
        to reach the target. Then, you check if you've already seen that complement in a previous step.
        """
        # Create a dictionary to store numbers we've seen and their indices.
        # The format will be {number: index}
        seen = {}

        # Enumerate gives us both the index (i) and the value (num)
        for i, num in enumerate(nums):
            # Calculate the number we need to find to reach the target
            complement = target - num
            
            # Check if this complement is already in our dictionary
            if complement in seen:
                # If it is, we've found our pair!
                # Return the index of the complement and the current index.
                return [seen[complement], i]
            
            # If the complement is not found, add the current number and its
            # index to the dictionary for future checks.
            seen[num] = i