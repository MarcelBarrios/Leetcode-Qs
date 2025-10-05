def max_non_adjacent_sum(nums):
    """
    Calculates the maximum sum of non-adjacent elements in a list.
    This is a classic dynamic programming problem (House Robber).

    :param nums: A list of positive integers.
    :return: The maximum possible sum.
    """
    # We use two variables to keep track of the max sums at previous steps.
    # rob1: max sum two steps back.
    # rob2: max sum one step back.
    rob1, rob2 = 0, 0
    
    # [rob1, rob2, n, n+1, ...]
    # For each number 'n' in our list...
    for n in nums:
        # We have a choice:
        # 1. Rob this house (n + rob1): Take the current value 'n' plus the max sum from two houses ago.
        # 2. Don't rob this house (rob2): Just take the max sum from the previous house.
        # 'temp' will store the new maximum loot.
        temp = max(n + rob1, rob2)
        
        # Now, we update our pointers for the next iteration.
        # The old 'rob2' becomes the new 'rob1' (two steps back).
        rob1 = rob2
        # Our newly calculated max loot 'temp' becomes the new 'rob2' (one step back).
        rob2 = temp
        
    # After the loop, rob2 will hold the overall maximum sum.
    return rob2

# Example Usage:
nums = [3, 4, 55, 23] 
print(f"For {nums}, the max non-adjacent sum is: {max_non_adjacent_sum(nums)}") # Expected: 58

nums2 = [2345, 54, 0, 0, 0, 0, 5, 34, 2]
print(f"For {nums2}, the max non-adjacent sum is: {max_non_adjacent_sum(nums2)}") # Expected: 2379 (2345 + 0 + 0 + 34)

nums3 = [2345, 54, 0, 0, 0, 0, 5, 34, 2000]
print(f"For {nums3}, the max non-adjacent sum is: {max_non_adjacent_sum(nums3)}") # Expected: 4379 (2345 + 0 + 0 + 2000)



