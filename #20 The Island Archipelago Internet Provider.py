# You are a project manager for a new internet service provider tasked with bringing 
# high-speed internet to a remote archipelago. The archipelago consists of several
# islands, and your company needs to lay undersea fiber-optic cables to connect them. 
# Your engineering team has provided you with a list of all possible connections 
# that can be made between pairs of islands and the cost to lay the cable for each 
# connection.

# Your goal is to connect all the islands so that they are part of a single network.
# This means that every island must be able to communicate with every other island, 
# either directly or indirectly through other islands. As the project manager, you 
# are under strict budget constraints, so you need to find the plan that connects 
# all the islands for the minimum possible total cost. You don't need to connect 
#     every island to every other one directly, just ensure they are all part of 
# one contiguous network.

# Your task is to write a program that takes the list of islands and the potential
# connections with their costs, and returns the minimum cost required to connect 
# the entire archipelago.

# Helper class for the Union-Find data structure
class UnionFind:
    def __init__(self, size):
        # Initialize each node to be its own parent.
        self.parent = list(range(size))
        # Optimization: keep track of the size of each set.
        self.rank = [1] * size

    def find(self, i):
        # Find the root parent of the set containing 'i'.
        # Path compression optimization: make every node on the path point to the root.
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        # Merge the sets containing 'i' and 'j'.
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by rank optimization: attach the smaller tree to the root of the larger tree.
            if self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            elif self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True # Return True if a merge happened.
        return False # Return False if they were already in the same set.

def solve_island_connections(num_islands, connections):
    """
    Calculates the minimum cost to connect all islands using Kruskal's algorithm.

    :param num_islands: The total number of islands.
    :param connections: A list of tuples, where each tuple is ((island1, island2), cost).
    :return: The minimum cost to connect all islands.
    """
    # Step 1: Sort all connections (edges) by their cost.
    connections.sort(key=lambda x: x[1])

    uf = UnionFind(num_islands)
    total_cost = 0
    num_edges = 0

    # Step 2: Iterate through the sorted connections.
    for (island1, island2), cost in connections:
        # Step 3: If the islands are not already connected, add the edge.
        if uf.union(island1, island2):
            total_cost += cost
            num_edges += 1
            # Optimization: stop when all islands are connected.
            if num_edges == num_islands - 1:
                break
    
    # Check if all islands are connected. If not, it's impossible.
    return total_cost if num_edges == num_islands - 1 else -1

# Example Usage:
islands = 4
cable_options = [((0, 1), 10), ((0, 2), 6), ((0, 3), 5), ((1, 3), 15), ((2, 3), 4)]
min_cost = solve_island_connections(islands, cable_options)
print(f"The minimum cost to connect all islands is: {min_cost}") # Expected output: 19
# O(E log E)