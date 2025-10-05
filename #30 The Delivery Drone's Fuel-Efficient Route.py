# You work for a futuristic logistics company that uses autonomous drones for last-mile delivery. You are
#  programming the navigation system for a new drone model. The city is represented as a 2D grid where 0
#  is an open flight path and 1 is a no-fly zone (a building or obstacle).

# The drone starts at the warehouse at (0, 0) and needs to deliver a package to a customer at a specific 
# target location. The drone can move up, down, left, or right.

# However, there's a new challenge. The city has strong, unpredictable winds. To navigate, the drone's 
# advanced motors sometimes need to perform a "power-boost" maneuver to cut through a building. This
# maneuver is costly and consumes a lot of energy. The drone is allowed to perform a maximum of k of 
# these power-boosts during its trip. Each power-boost allows it to fly through exactly one building cell (1).

# Your task is to write a program that finds the shortest possible delivery route (minimum number of steps)
# from the warehouse (0, 0) to the target, given that the drone can break through at most k obstacles.

from collections import deque

def find_drone_route(grid, k):
    """
    Finds the shortest path for a delivery drone that can break through 'k' obstacles.

    This problem is an extension of the classic shortest path on a grid problem. A standard BFS would stop 
    at the first obstacle. Here, we need to find the shortest path while also keeping track of an additional
    piece of "state": the number of obstacles we've broken through.

    This makes it a perfect fit for a modified Breadth-First Search (BFS). Instead of just tracking visited cells,
    we need to track visited states. A "state" will be a combination of a cell's coordinates and the number of 
    obstacles broken to get there.

    :param grid: A 2D list of 0s (open) and 1s (obstacles).
    :param k: The maximum number of obstacles the drone can break.
    :return: The length of the shortest path, or -1 if unreachable.
    """
    rows, cols = len(grid), len(grid[0])
    target = (rows - 1, cols - 1)

    # The queue will store (row, col, obstacles_broken, steps).
    queue = deque([(0, 0, 0, 0)])
    
    # 'visited' will store tuples of (row, col, obstacles_broken) to track states.
    visited = set([(0, 0, 0)])
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, obs_broken, steps = queue.popleft()

        # If we've reached the target, return the steps taken.
        if (r, c) == target:
            return steps

        # Explore the four neighbors.
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check if the neighbor is within the grid boundaries.
            if 0 <= nr < rows and 0 <= nc < cols:
                # Case 1: The neighbor is an open path.
                if grid[nr][nc] == 0:
                    # If we haven't visited this cell with the current number of breaks, add it.
                    if (nr, nc, obs_broken) not in visited:
                        visited.add((nr, nc, obs_broken))
                        queue.append((nr, nc, obs_broken, steps + 1))
                
                # Case 2: The neighbor is an obstacle.
                elif grid[nr][nc] == 1:
                    # If we still have power-boosts left...
                    if obs_broken < k:
                        # ...and we haven't visited this cell having broken one more obstacle...
                        if (nr, nc, obs_broken + 1) not in visited:
                            visited.add((nr, nc, obs_broken + 1))
                            queue.append((nr, nc, obs_broken + 1, steps + 1))
    
    # If the queue is empty and we haven't reached the target, it's impossible.
    return -1
# Let R be the number of rows, C be the number of columns, and K be the max number of obstacles to break.

# Time Complexity: O(R * C * K)

# The number of possible states is R * C * K, since each cell can be visited with 0, 1, ..., K obstacles broken.

# Our BFS ensures that we visit each unique state at most once. Therefore, the time complexity is proportional to the total number of states.

# Example Usage:
city_grid = [
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0],
    [0, 1, 1],
    [0, 0, 0]
]
max_boosts = 1
# The drone needs to break the obstacle at (3,1) to find the shortest path.
shortest_path = find_drone_route(city_grid, max_boosts)
print(f"The shortest delivery route takes: {shortest_path} steps") # Expected output: 8