# You are the lead cryptographer for an international spy agency. Your network consists of several agents 
# stationed in different cities around the world. For security, agents can only communicate directly with 
# a few other specific agents through encrypted channels. Each communication channel has a different 
# transmission delay, meaning it takes a certain amount of time for a message to be relayed from one agent 
# to another.

# A critical piece of intelligence has just been acquired by a source agent, and it must be delivered to a
# target agent as quickly as possible. The message may need to be relayed through several other agents in 
# the network to reach its destination.

# Your task is to write a program that can, given the network map (which agents can talk to whom and the 
# time delays), find the absolute minimum time it will take for the message to travel from the source agent 
# to the target agent.

import heapq

def find_fastest_route(num_agents, channels, source, target):
    """
    Finds the fastest time to send a message between two agents in a network
    using Dijkstra's algorithm.

    This problem is a classic "shortest path in a weighted graph" problem. Since the "costs" (time delays)
      are all non-negative, the perfect algorithm for this is Dijkstra's Algorithm.

    Dijkstra's algorithm finds the shortest path from a single source node to all other nodes in a graph. 
    It works by progressively finding the "closest" unvisited node and exploring its neighbors.

    :param num_agents: The total number of agents.
    :param channels: A list of tuples (agent1, agent2, time).
    :param source: The ID of the source agent.
    :param target: The ID of the target agent.
    :return: The minimum time required, or -1 if unreachable.
    """
    # Step 1: Build the adjacency list graph.
    graph = {i: [] for i in range(num_agents)}
    for u, v, time in channels:
        graph[u].append((v, time))
        # If channels are two-way, add the reverse path as well.
        # graph[v].append((u, time))

    # Step 2: Initialize distances and the priority queue.
    distances = {agent: float('inf') for agent in range(num_agents)}
    distances[source] = 0
    priority_queue = [(0, source)]  # (time_to_reach, agent_id)

    # Step 3: The Algorithm Loop
    while priority_queue:
        # Pop the agent that is currently closest to the source.
        current_time, current_agent = heapq.heappop(priority_queue)

        # Optimization: If we've already found a shorter path to this agent, skip.
        if current_time > distances[current_agent]:
            continue

        # Explore the neighbors of the current agent.
        for neighbor, time_to_neighbor in graph[current_agent]:
            new_time = current_time + time_to_neighbor

            # Step 4: The Relaxation Step
            # If we've found a shorter path to the neighbor...
            if new_time < distances[neighbor]:
                # ...update its distance and push it to the queue.
                distances[neighbor] = new_time
                heapq.heappush(priority_queue, (new_time, neighbor))

    # Step 5: Final Answer
    final_time = distances[target]
    return final_time if final_time != float('inf') else -1
# Let V be the number of agents (vertices) and E be the number of communication channels (edges).

# Time Complexity: O(E log V)

# The most time-consuming part is the while loop. In the worst case, every edge will result in a heappush operation into the priority queue.

# A heappush or heappop operation on a priority queue of size V takes O(log V) time.

# Since we do this for up to E edges, the total time complexity is O(E log V).

# Example Usage:
num_spies = 4
spy_channels = [(0, 1, 2), (0, 2, 5), (1, 2, 1), (1, 3, 6), (2, 3, 2)]
source_agent = 0
target_agent = 3
min_time = find_fastest_route(num_spies, spy_channels, source_agent, target_agent)
print(f"The minimum time to send the message is: {min_time} hours") # Expected output: 5

# Solution 2

def find_fastest_route_bellman_ford(num_agents, channels, source, target):
    """
    Finds the fastest time to send a message between two agents in a network
    using the Bellman-Ford algorithm.

    The idea behind Bellman-Ford algo is to start with an estimate of the shortest time to each agent and then
    iteratively improve that estimate. It does this by "relaxing" every single communication channel in
    the network, and it repeats this process multiple times.

    :param num_agents: The total number of agents.
    :param channels: A list of tuples (agent1, agent2, time).
    :param source: The ID of the source agent.
    :param target: The ID of the target agent.
    :return: The minimum time required, or -1 if unreachable.
    """
    # Step 1: Initialize distances.
    # The source is 0, and all others are effectively unreachable (infinity).
    distances = {agent: float('inf') for agent in range(num_agents)}
    distances[source] = 0

    # Step 2: Relax all edges repeatedly.
    # This loop runs V-1 times (where V is num_agents).
    for _ in range(num_agents - 1):
        # In each iteration, we go through every single communication channel.
        for u, v, time in channels:
            # If we've found a path to agent 'u'...
            if distances[u] != float('inf'):
                # ...and the path to 'v' through 'u' is shorter...
                if distances[u] + time < distances[v]:
                    # ...we update the shortest time to reach 'v'.
                    distances[v] = distances[u] + time

    # Step 3: Final Answer
    final_time = distances[target]
    return final_time if final_time != float('inf') else -1
# Let V be the number of agents (vertices) and E be the number of communication channels (edges).

# Time Complexity: O(V * E)

# The algorithm has a main loop that runs V-1 times.

# Inside this loop, it iterates through all E channels.

# This gives a total time complexity of (V-1) * E, which simplifies to O(V * E). This is generally slower than Dijkstra's O(E log V) on most graphs.

# Example Usage:
num_spies = 4
spy_channels = [(0, 1, 2), (0, 2, 5), (1, 2, 1), (1, 3, 6), (2, 3, 2)]
source_agent = 0
target_agent = 3
min_time = find_fastest_route_bellman_ford(num_spies, spy_channels, source_agent, target_agent)
print(f"The minimum time to send the message (Bellman-Ford) is: {min_time} hours") # Expected output: 5