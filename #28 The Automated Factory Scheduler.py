# You are in charge of programming the production schedule for a new, fully automated factory. The factory has 
# several different machines, each dedicated to producing the same type of widget. However, due to their 
# different ages and designs, each machine works at a different speed. You are given a list of machine_speeds,
# where each element represents the number of minutes it takes for that specific machine to produce a single
#  widget. All machines can work in parallel.

# Today, the factory has received a large order for a specific number of total_widgets. Your manager wants to 
# know the absolute minimum amount of time the factory must run to complete this order.

# Your task is to write a function that takes the list of machine speeds and the total number of widgets 
# required, and returns the minimum number of minutes needed to produce them.

def solve_factory_schedule(machine_speeds, total_widgets):
    """
    Calculates the minimum time needed for a set of machines to produce a target number of widgets.

    This problem asks for the minimum time to achieve a goal. A simple approach would be to simulate the 
    factory minute by minute, but that would be far too slow for a large order. A much more efficient
    solution is to use Binary Search on the Answer.

    :param machine_speeds: A list of integers representing minutes per widget for each machine.
    :param total_widgets: The target number of widgets to produce.
    :return: The minimum integer number of minutes required.
    """
    if total_widgets == 0:
        return 0

    # Helper function to check if a given time is sufficient.
    def can_produce(time):
        produced_count = 0
        for speed in machine_speeds:
            produced_count += time // speed
        return produced_count >= total_widgets

    # Define the search space for the binary search.
    left = 1
    # A safe upper bound: the time for the fastest machine to do the whole job.
    right = min(machine_speeds) * total_widgets
    min_required_time = right

    # Perform binary search on the answer (time).
    while left <= right:
        mid_time = left + (right - left) // 2
        
        # If this mid_time is a possible solution...
        if can_produce(mid_time):
            # ...store it as our best answer so far and try for an even smaller time.
            min_required_time = mid_time
            right = mid_time - 1
        else:
            # ...this time is not enough, so we need to search for a larger time.
            left = mid_time + 1
            
    return min_required_time
# Let N be the number of machines and M be the value of the upper bound of our search space (e.g., fastest_speed * target).

# Time Complexity: O(N * log M)

# The binary search performs log M iterations.

# Inside each iteration, we call the can_produce function, which loops through all N machines once.

# This gives a total time complexity of O(N * log M).

# Example Usage:
speeds = [2, 3, 5]
target = 10
time_needed = solve_factory_schedule(speeds, target)
print(f"Minimum time needed to produce {target} widgets: {time_needed} minutes") # Expected output: 10

speeds_2 = [1, 10, 100]
target_2 = 100
time_needed_2 = solve_factory_schedule(speeds_2, target_2)
print(f"Minimum time needed to produce {target_2} widgets: {time_needed_2} minutes") # Expected output: 90
# In 89 mins: 89//1 + 89//10 + 89//100 = 89+8+0 = 97 (not enough)
# In 90 mins: 90//1 + 90//10 + 90//100 = 90+9+0 = 99 (not enough)
# In 91 mins: 91//1 + 91//10 + 91//100 = 91+9+0 = 100 (enough) - whoops, let me re-check logic.
# Ah, my example walkthrough was slightly off. The final answer should be the first time it passes.
# Let's re-run example 1:
# mid_time=8, produced=7 (False). left=9.
# mid_time=9, produced=8 (False). left=10.
# search space [10, 9]. left > right, loop ends. returns 10.
# The logic holds, my manual trace was slightly off. Let me correct the second example's expected output.
# For example 2:
# Search space [1, 100]. mid = 50. produce(50) = 50+5+0=55 (False). left=51.
# Search space [51, 100]. mid=75. produce(75)=75+7+0=82 (False). left=76.
# Search space [76, 100]. mid=88. produce(88)=88+8+0=96 (False). left=89.
# Search space [89, 100]. mid=94. produce(94)=94+9+0=103 (True). ans=94, right=93.
# Search space [89, 93]. mid=91. produce(91)=91+9+0=100 (True). ans=91, right=90.
# Search space [89, 90]. mid=89. produce(89)=89+8+0=97 (False). left=90.
# Search space [90, 90]. mid=90. produce(90)=90+9+0=99 (False). left=91.
# search space [91, 90]. left > right, loop ends. returns 91.
print(f"Minimum time needed to produce {target_2} widgets: {time_needed_2} minutes") # Corrected expected output: 91