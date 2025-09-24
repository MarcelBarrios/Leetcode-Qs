# You are the captain of a pirate ship, and you've just discovered a treasure island 
# containing several piles of gold. Each pile of gold has a specific monetary value 
# and a specific weight. Your ship, however, is not very large and has a maximum 
# weight capacity it can carry.

# You are faced with a classic pirate's dilemma: you want to steal as much gold as
#  possible to maximize your riches, but you cannot overload your ship. For each 
#  pile of gold, you must make a decision: either you take the entire pile, or 
#  you leave it behind. You cannot take a fraction of a pile.

# Your task is to write a program that determines the maximum total value of gold 
# you can carry away from the island without sinking your ship.

def solve_pirate_treasure(gold_piles, capacity):
    """
    Calculates the maximum value of gold a pirate can steal using the 0/1 Knapsack algorithm.

    :param gold_piles: A list of tuples, where each tuple is (value, weight).
    :param capacity: The maximum weight the ship can carry.
    :return: The maximum value of gold that can be carried.
    """
    num_piles = len(gold_piles)
    
    # Create a DP table to store the maximum value for subproblems.
    # dp[i][w] will be the max value using first 'i' piles with capacity 'w'.
    # Initialize all values to 0.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(num_piles + 1)]

    # Iterate through each pile of gold.
    for i in range(1, num_piles + 1):
        # The -1 is because our dp table is 1-indexed for convenience, but the list is 0-indexed.
        value, weight = gold_piles[i-1]
        
        # Iterate through each possible weight capacity.
        for w in range(1, capacity + 1):
            # Option 1: Don't take the current pile of gold.
            # The value is the same as the best we could do with the previous piles.
            dont_take_value = dp[i-1][w]
            
            # Option 2: Take the current pile of gold, if it fits.
            take_value = 0
            if weight <= w:
                # The value is the current pile's value plus the best value for the remaining capacity.
                take_value = value + dp[i-1][w - weight]
            
            # The optimal choice is the maximum of taking or not taking the pile.
            dp[i][w] = max(dont_take_value, take_value)
            
    # The bottom-right cell contains the solution for all piles and the full capacity.
    return dp[num_piles][capacity]

# Example Usage:
piles = [(60, 10), (100, 20), (120, 30)]
ship_capacity = 50
max_value = solve_pirate_treasure(piles, ship_capacity)
# The optimal choice is to take piles (100, 20) and (120, 30), total value 220, total weight 50.
print(f"The maximum value the pirate can steal is: {max_value}") # Expected output: 220
# O(n * W)