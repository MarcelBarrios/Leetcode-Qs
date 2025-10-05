# You are programming the software for a new, advanced vending machine. A customer has just bought an item, 
# and the machine needs to provide the correct change. The machine has a limited set of coin denominations 
# it can dispense (for example, it has an unlimited supply of pennies, nickels, dimes, and quarters).

# To be as efficient as possible and to conserve its coin supply, the machine must always give back the 
# change using the fewest possible number of coins.

# Your task is to write a function that, given a list of available coin denominations and a total amount 
# of change to be made, calculates the minimum number of coins required to make that exact amount. If it's
# impossible to make the change with the given coins (for example, trying to make 7 cents with only dimes),
# the function should indicate that.

def make_change(coins, amount):
    """
    This problem is a classic example of what's known as the Unbounded Knapsack problem, and it can be
    solved perfectly using bottom-up Dynamic Programming. The core idea is to solve the problem for 
    smaller amounts first and use those results to solve for larger amounts.

    :param coins: A list of available coin denominations.
    :param amount: The target amount of change.
    :return: The minimum number of coins, or -1 if impossible.
    """
    # Create a DP array to store the minimum coins for each amount from 0 to 'amount'.
    # Initialize with a value larger than any possible solution (infinity).
    dp = [float('inf')] * (amount + 1)
    
    # The minimum coins to make amount 0 is 0 coins.
    dp[0] = 0
    
    # Iterate through each amount from 1 up to the target amount.
    for a in range(1, amount + 1):
        # For each amount, try to make it using each available coin.
        for coin in coins:
            # If the current coin can be used (it's not larger than the amount)...
            if coin <= a:
                # ...the number of coins needed would be 1 (this coin) plus the
                # minimum coins needed for the rest of the amount (a - coin).
                # We update our table with the minimum value found so far for this amount.
                dp[a] = min(dp[a], 1 + dp[a - coin])
                
    # After filling the table, the final answer is in the last cell.
    # If the value is still infinity, it means the amount could not be made.
    return dp[amount] if dp[amount] != float('inf') else -1
# Let A be the target amount and C be the number of coin denominations.

# Time Complexity: O(A * C)
# The algorithm consists of two nested loops. The outer loop runs A times (for each amount), and the inner loop runs C times (for each coin).

# Example Usage:
coin_denominations = [1, 2, 5]
change_due = 11
min_coins = make_change(coin_denominations, change_due)
print(f"Minimum coins to make {change_due} cents: {min_coins}") # Expected output: 3

coin_denominations_2 = [2]
change_due_2 = 3
min_coins_2 = make_change(coin_denominations_2, change_due_2)
print(f"Minimum coins to make {change_due_2} cents: {min_coins_2}") # Expected output: -1

# Solution 2
def make_change_memoization(coins, amount):
    """
    Calculates the minimum number of coins required to make a specific amount
    using a top-down recursive approach with memoization.

    The core idea is to create a recursive function that solves for a given amount. We'll use a "memo"
    (a cache, like an array or dictionary) to store the results of amounts we've already calculated,
    so we never have to solve the same subproblem twice.

    :param coins: A list of available coin denominations.
    :param amount: The target amount of change.
    :return: The minimum number of coins, or -1 if impossible.
    """
    # Create a cache (memo) to store the results of subproblems.
    # Initialize with -1 to indicate that the subproblem has not been solved yet.
    memo = [-1] * (amount + 1)

    def find_min_coins(target):
        # --- Base Cases ---
        # If the target is 0, we need 0 coins.
        if target == 0:
            return 0
        # If the target is negative, this is an invalid path.
        if target < 0:
            return float('inf')

        # --- Check the Cache ---
        # If we have already computed the answer for this target, return it.
        if memo[target] != -1:
            return memo[target]

        # --- Recursive Exploration ---
        # Initialize the minimum coins for this target to infinity.
        min_coins_for_target = float('inf')

        # Try using each coin to reach the target.
        for coin in coins:
            # Recursively solve for the remaining amount.
            result = find_min_coins(target - coin)

            # If the recursive call found a valid solution (not infinity)...
            if result != float('inf'):
                # ...update our minimum for the current target.
                # The total is 1 (for the current coin) + the result for the rest.
                min_coins_for_target = min(min_coins_for_target, 1 + result)
        
        # --- Store and Return ---
        # Store the computed minimum in our cache.
        memo[target] = min_coins_for_target
        return min_coins_for_target

    # Kick off the recursion for the initial amount.
    final_result = find_min_coins(amount)

    # If the result is still infinity, it means the amount was impossible to make.
    return final_result if final_result != float('inf') else -1
# Time Complexity: O(A * C)

# Because of memoization, the recursive function find_min_coins(target) is computed only once for each target from 0 to A.

# Inside each computation, there is a loop that runs C times (for each coin).

# This results in the same time complexity as the bottom-up approach.

# Example Usage:
coin_denominations = [1, 2, 5]
change_due = 11
min_coins = make_change_memoization(coin_denominations, change_due)
print(f"Minimum coins to make {change_due} cents (memoization): {min_coins}") # Expected output: 3