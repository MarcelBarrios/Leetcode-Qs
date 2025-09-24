# Of course. Here is your fourth story-driven problem. This one models a common 
# real-world scenario—dependencies—using a graph data structure.

# Problem 4: The University Course Planner
# The Story:
# You are a computer science student planning your degree, and you're faced with a 
# classic challenge: course prerequisites. The university provides you with the 
# total number of courses you need to take, labeled from 0 to n-1, and a list of
# prerequisite pairs. A pair [A, B] means that you must complete course B before 
# you can enroll in course A.

# Your goal is to determine if it's possible to finish all the courses. It's possible
# to finish them all unless there is a logical impossibility in the requirements. 
# For instance, if Course 1 requires you to first take Course 0, but Course 0 
# requires you to first take Course 1, you have a circular dependency, and it's
# impossible to complete your degree.

# Your task is to write a program that takes the total number of courses and the
# list of prerequisites and returns True if you can finish all courses, and False 
# otherwise.

def can_finish_courses(numCourses, prerequisites):
    """
    Determines if all courses can be completed given the prerequisite requirements.
    This is equivalent to detecting a cycle in a directed graph.

    :param numCourses: The total number of courses.
    :param prerequisites: A list of pairs [course, prerequisite].
    :return: True if all courses can be finished, False otherwise.
    """
    # Step 1: Build the adjacency list representation of the graph.
    # The key is the prerequisite, the value is a list of courses that depend on it.
    adj_list = {i: [] for i in range(numCourses)}
    for course, prereq in prerequisites:
        adj_list[prereq].append(course)

    # Sets to track the state of each course during DFS.
    visiting = set() # Courses currently in our recursion stack (path).
    visited = set()  # Courses that have been fully explored and are safe.

    def has_cycle(course):
        # Add the current course to the set of nodes we are currently visiting.
        visiting.add(course)

        # Explore all neighbors (courses that depend on the current course).
        for neighbor in adj_list[course]:
            # If the neighbor is already in our current visiting path, we have a cycle.
            if neighbor in visiting:
                return True # Cycle detected!
            
            # If the neighbor has not been fully visited yet, perform DFS from it.
            if neighbor not in visited:
                if has_cycle(neighbor):
                    return True # A cycle was found deeper in the recursion.

        # Backtrack: Remove the course from the visiting set as we leave its path.
        visiting.remove(course)
        # Mark this course as fully visited and safe.
        visited.add(course)
        
        # No cycle was found originating from this course.
        return False

    # Check for cycles starting from every course.
    for course in range(numCourses):
        # We only need to start a new DFS for courses we haven't fully visited yet.
        if course not in visited:
            if has_cycle(course):
                # If a cycle is found at any point, we know it's impossible.
                return False
    
    # If we check all courses and find no cycles, it's possible.
    return True

# Example Usage:
num_courses = 4
# Prereqs: 1->0, 2->1, 3->2
possible_schedule = [[0, 1], [1, 2], [2, 3]] 
print(f"Is the possible schedule completable? {can_finish_courses(num_courses, possible_schedule)}") # Expected: True

# Prereqs: 1->0, 0->1
impossible_schedule = [[0, 1], [1, 0]]
print(f"Is the impossible schedule completable? {can_finish_courses(2, impossible_schedule)}") # Expected: False
# O(V + E)