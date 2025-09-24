# You've been hired by a massive e-commerce company to optimize their warehouse
# operations. Inside the warehouse, a single robot is responsible for fetching 
# items from shelves. The warehouse floor is represented by a 2D grid. Some cells 
# in the grid are empty floor space that the robot can travel on, while other 
# cells are shelves or other obstacles that the robot cannot pass through.

# The robot can move up, down, left, or right, but it cannot move diagonally or go 
# through obstacles. Each move from one empty cell to an adjacent one costs 1 unit 
# of energy (i.e., takes 1 step).

# Your task is to write a program that calculates the minimum number of steps the 
# robot must take to travel from its starting position to the location of a 
# specific item. If it's impossible for the robot to reach the item, your program 
# should indicate that.

# ## Example 
# Input:

# grid =
# [['S', '.', '.', '#'],
#  ['.', '#', '.', '.'],
#  ['.', '#', '.', 'T'],
#  ['.', '.', '.', '.']]
# (S=Start, T=Target, .=Empty, #=Obstacle)

# start = (0, 0)

# target = (2, 3)

# Final Result:

# The robot reaches the target at (2, 3) with a distance of 7. The function returns 7.



from collections import deque

def find_shortest_path(grid):
    """
    Finds the shortest path for a robot in a warehouse grid.

    :param grid: A 2D list representing the warehouse.
    :return: The minimum number of steps, or -1 if the target is unreachable.

    This problem is a classic example of finding the shortest path in an unweighted 
    grid, which is a perfect use case for the Breadth-First Search (BFS) algorithm.

    BFS explores the grid layer by layer, starting from the robot's initial position.
    It guarantees that when we first find the target item, we have found it via the
    shortest possible path.
    """
    # Find grid dimensions and the start/target positions.
    rows, cols = len(grid), len(grid[0])
    start_pos, target_pos = None, None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_pos = (r, c)
            elif grid[r][c] == 'T':
                target_pos = (r, c)

    if not start_pos or not target_pos:
        return -1 # Start or Target not found

    # Initialize the queue for BFS with (position, distance).
    queue = deque([(start_pos, 0)])
    # Keep track of visited cells to avoid cycles.
    visited = {start_pos}
    
    # Define the possible moves (up, down, left, right).
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Process the queue until it's empty.
    while queue:
        # Get the current position and distance from the front of the queue.
        (current_row, current_col), distance = queue.popleft()

        # If we've reached the target, return the distance.
        if (current_row, current_col) == target_pos:
            return distance

        # Explore all four neighbors.
        for dr, dc in directions:
            next_row, next_col = current_row + dr, current_col + dc

            # Check if the neighbor is within the grid boundaries.
            if 0 <= next_row < rows and 0 <= next_col < cols:
                # Check if the neighbor is a valid path and hasn't been visited.
                if grid[next_row][next_col] != '#' and (next_row, next_col) not in visited:
                    # Mark the neighbor as visited.
                    visited.add((next_row, next_col))
                    # Add the neighbor to the queue with the new distance.
                    queue.append(((next_row, next_col), distance + 1))
    
    # If the queue becomes empty and we haven't found the target, it's unreachable.
    return -1
# O(R * C)

# Example Usage:
warehouse_grid = [
    ['S', '.', '.', '#'],
    ['.', '#', '.', '.'],
    ['.', '#', '.', 'T'],
    ['.', '.', '.', '.']
]
print(f"The shortest path is: {find_shortest_path(warehouse_grid)} steps") # Expected output: 7


# Solution 2
def find_shortest_path_dfs(grid):
    """
    Finds the shortest path for a robot using Depth-First Search.

    :param grid: A 2D list representing the warehouse.
    :return: The minimum number of steps, or -1 if the target is unreachable.
    """
    # Find grid dimensions and the start/target positions.
    rows, cols = len(grid), len(grid[0])
    start_pos = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_pos = (r, c)

    if not start_pos:
        return -1 # Start not found

    # Use a list to store the minimum distance, allowing it to be modified within the recursion.
    min_distance = [float('inf')]
    # Keep track of visited cells for the current path.
    visited = set()

    # Define the recursive DFS helper function.
    def dfs(row, col, steps):
        # --- Boundary and Obstacle Checks ---
        if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] == '#' or (row, col) in visited:
            return

        # --- Target Found ---
        if grid[row][col] == 'T':
            # We found a path. See if it's the shortest one yet.
            min_distance[0] = min(min_distance[0], steps)
            return

        # --- Explore ---
        # Mark the current cell as visited for this path.
        visited.add((row, col))
        
        # Recursively explore all four neighbors.
        dfs(row + 1, col, steps + 1)  # Down
        dfs(row - 1, col, steps + 1)  # Up
        dfs(row, col + 1, steps + 1)  # Right
        dfs(row, col - 1, steps + 1)  # Left

        # --- Backtrack ---
        # Un-mark the cell so other paths can use it. This is crucial.
        visited.remove((row, col))

    # Start the DFS from the starting position with 0 steps.
    dfs(start_pos[0], start_pos[1], 0)

    # If min_distance was never updated, the target is unreachable.
    return min_distance[0] if min_distance[0] != float('inf') else -1

# Example Usage:
warehouse_grid = [
    ['S', '.', '.', '#'],
    ['.', '#', '.', '.'],
    ['.', '#', '.', 'T'],
    ['.', '.', '.', '.']
]
print(f"The shortest path using DFS is: {find_shortest_path_dfs(warehouse_grid)} steps")
# O(4^(R*C)) 