# You work at a fruit distribution center. A new shipment of oranges has arrived, packed into a rectangular crate represented by a 2D grid. In this grid, each cell can have one of three values: 0 representing an empty space, 1 representing a fresh orange, or 2 representing a rotten orange.

# The problem is that rot spreads very quickly. Every minute, any fresh orange that is horizontally or vertically adjacent to a rotten orange becomes rotten itself. The rot cannot spread diagonally or through empty spaces.

# Your manager needs to know how long it will take for the entire crate to go bad so they can prioritize shipments. Your task is to write a program that calculates the minimum number of minutes that must elapse until no fresh oranges remain. If some oranges will never rot because they are isolated, the process is impossible, and your program should reflect that.
    
from collections import deque

def time_to_rot(grid):
    """
    Calculates the minimum time for all fresh oranges to rot.

    This problem is a perfect fit for a Multi-Source Breadth-First Search (BFS). It's a BFS because we want to find the shortest time, and the "rot" spreads in layers, one minute at a time. It's "multi-source" because the rot can start from multiple oranges simultaneously.

    :param grid: A 2D list representing the crate of oranges.
    :return: The minimum minutes required, or -1 if impossible.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges_count = 0

    # Initial scan to set up the BFS.
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh_oranges_count += 1
            elif grid[r][c] == 2:
                # Add all initially rotten oranges to the queue as starting points.
                queue.append((r, c, 0)) # (row, col, minutes)

    # If there are no fresh oranges to begin with, the time is 0.
    if fresh_oranges_count == 0:
        return 0

    minutes_elapsed = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Start the multi-source BFS.
    while queue:
        r, c, minutes = queue.popleft()
        
        # Keep track of the maximum time elapsed.
        minutes_elapsed = max(minutes_elapsed, minutes)

        # Explore the 4 adjacent cells.
        for dr, dc in directions:
            next_r, next_c = r + dr, c + dc

            # Check if the neighbor is a valid, fresh orange.
            if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == 1:
                # It becomes rotten.
                grid[next_r][next_c] = 2
                # We've processed one more fresh orange.
                fresh_oranges_count -= 1
                # Add it to the queue for the next minute.
                queue.append((next_r, next_c, minutes + 1))
    
    # After the BFS, if there are still fresh oranges, it's impossible.
    return minutes_elapsed if fresh_oranges_count == 0 else -1

# Example Usage:
crate = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
time = time_to_rot(crate)
print(f"Minimum time for all oranges to rot: {time} minutes") # Expected output: 4

crate_impossible = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
time_impossible = time_to_rot(crate_impossible)
print(f"Minimum time for impossible crate: {time_impossible} minutes") # Expected output: -1