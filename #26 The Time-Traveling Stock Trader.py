# Imagine you are a brilliant stock trader who has just invented a limited time machine. Your machine 
# allows you to see the future stock prices for a single, volatile tech stock over the next N days. 
# You are given a list of these daily stock prices.

# Your trading strategy is simple: you can buy one share of the stock on any given day, and then sell
# that same share on any later day. You can perform this buy-sell transaction as many times as you want.
# However, there is a physical limitation: you can only hold one share of the stock at a time. This 
# means you must sell your current share before you are allowed to buy another one.

# Your goal is to use your knowledge of the future to calculate the maximum possible profit you can make
# by the end of the N-day period.

def maximize_stock_profit(prices):
    """
    Calculates the maximum profit from buying and selling a stock multiple times using greedy algorithm.

    The key insight is that you don't need to hold a stock for a long time to maximize profit. The total
    profit from a long upward trend (e.g., buying at $10 and selling at $50) is the same as the sum of
    all the small, day-to-day profits within that trend (e.g., buying at $10, selling at $20; buying
    at $20, selling at $35, etc.).

    This means we can simplify our strategy to a single rule: collect every single profit you can, no 
    matter how small.

    :param prices: A list of daily stock prices.
    :return: The maximum possible profit.
    """
    # If we have less than two days, no transaction is possible.
    if not prices or len(prices) < 2:
        return 0

    total_profit = 0

    # Iterate through the prices starting from the second day.
    for i in range(1, len(prices)):
        # Check if the current day's price is higher than the previous day's.
        if prices[i] > prices[i-1]:
            # If so, we've found a profitable "buy yesterday, sell today" opportunity.
            # Add this guaranteed profit to our total.
            total_profit += prices[i] - prices[i-1]
            
    return total_profit

# Let N be the number of days (the length of the prices list).

# Time Complexity: O(N)
# The algorithm involves a single pass through the prices array. The number of operations is directly proportional to the number of days.

# Example Usage:
stock_prices = [7, 1, 5, 3, 6, 4]
max_profit = maximize_stock_profit(stock_prices)
print(f"The maximum profit the trader can make is: ${max_profit}") # Expected output: 7

stock_prices_2 = [1, 2, 3, 4, 5]
max_profit_2 = maximize_stock_profit(stock_prices_2)
# Here, profit is (2-1)+(3-2)+(4-3)+(5-4) = 4, which is the same as buying at 1 and selling at 5.
print(f"The maximum profit for the second stock is: ${max_profit_2}") # Expected output: 4

# Solution 2
def maximize_stock_profit_peak_valley(prices):
    """
    Calculates the maximum profit from buying and selling a stock multiple times
    by finding and transacting on peaks and valleys.

    The idea is to model the stock prices as a landscape of hills and valleys. Our goal is to buy at the
    bottom of a hill (a valley) and sell at the top of that same hill (the next peak). We can repeat 
    this for every hill we find.

    :param prices: A list of daily stock prices.
    :return: The maximum possible profit.
    """
    if not prices or len(prices) < 2:
        return 0

    total_profit = 0
    i = 0
    n = len(prices)

    # Loop through the entire list of prices.
    while i < n - 1:
        # --- Find the next Valley (buy point) ---
        # Keep advancing 'i' as long as the price is decreasing.
        while i < n - 1 and prices[i] >= prices[i+1]:
            i += 1
        
        # If we reached the end while prices were only decreasing, no profit is possible.
        if i == n - 1:
            break
            
        # We found a valley. This is our buy point.
        buy_price = prices[i]
        
        # Move to the next day to start looking for a peak.
        i += 1

        # --- Find the next Peak (sell point) ---
        # Keep advancing 'i' as long as the price is increasing.
        while i < n - 1 and prices[i] <= prices[i+1]:
            i += 1

        # We either found a peak or reached the end of the list.
        # The day before the price started dropping again is our sell point.
        sell_price = prices[i]

        # Add the profit from this transaction to our total.
        total_profit += sell_price - buy_price
        
        # Move to the next day to start looking for the next transaction.
        i += 1
            
    return total_profit
# Let N be the number of days (the length of the prices list).

# Time Complexity: O(N)
# Even though there are nested while loops, the pointer i is only ever incremented and never reset. It traverses the entire array exactly once, making the time complexity linear.

# Example Usage:
stock_prices = [7, 1, 5, 3, 6, 4]
max_profit = maximize_stock_profit_peak_valley(stock_prices)
print(f"The maximum profit (Peak/Valley) is: ${max_profit}") # Expected output: 7

stock_prices_2 = [1, 2, 3, 4, 5]
max_profit_2 = maximize_stock_profit_peak_valley(stock_prices_2)
print(f"The maximum profit for the second stock (Peak/Valley) is: ${max_profit_2}") # Expected output: 4