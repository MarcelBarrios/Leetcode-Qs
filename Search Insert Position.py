# 35. Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the
#  index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
 
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        repeatedly divide the search interval in half. If the value of the search key is less than 
        the item in the middle of the interval, we narrow the interval to the lower half. Otherwise, 
        we narrow it to the upper half. We continue this until the value is found or the interval is empty.
        """
        # Initialize pointers for the start and end of the array.
        left, right = 0, len(nums) - 1
        
        # Loop as long as the search range is valid.
        # O(log n)
        while left <= right:
            # Calculate the middle index to avoid potential overflow.
            mid = left + (right - left) // 2
            
            # Case 1: The target is found at the middle index.
            if nums[mid] == target:
                return mid
            
            # Case 2: The target is greater than the middle element.
            # Search the right half of the array.
            elif nums[mid] < target:
                left = mid + 1
            
            # Case 3: The target is smaller than the middle element.
            # Search the left half of the array.
            else:
                right = mid - 1
        
        # If the loop finishes, the target was not found.
        # 'left' is now the index where the target should be inserted.
        return left
# O(log n)