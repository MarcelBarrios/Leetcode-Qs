# You are a DJ preparing for a major music festival. For the grand finale of your set, you have selected 
# a handful of your most iconic, "must-play" songs. The order in which you play these final songs is 
# critical to the energy of the crowd, and you believe there's a perfect sequence, but you're not sure what
# it is.

# To figure it out, you decide to generate every single possible ordering of these must-play songs. By 
# looking at all possible "setlists," you can then manually pick the one that you feel has the best flow.

# Your task is to write a program that takes a list of unique song titles and generates a list of all 
# possible setlists (i.e., all possible permutations of the songs).

def generate_setlists(songs):
    """
    Generates all possible orderings (permutations) of a list of songs.

    This problem asks us to find all permutations of a set of items, which is a textbook case for a 
    recursive algorithm called backtracking. The strategy is to build each possible setlist one song at 
    a time. For each position in the setlist, we will try placing every available song.

    :param songs: A list of unique song titles.
    :return: A list of all possible setlists (a list of lists).
    """
    # This list will store all the complete permutations.
    all_permutations = []
    # A boolean array to keep track of which songs have been used in the current permutation.
    used = [False] * len(songs)

    def find_permutations(current_setlist):
        """
        A recursive helper function that builds a permutation.
        :param current_setlist: The list of songs chosen so far.
        """
        # Base Case: If the current setlist is complete, we've found one permutation.
        if len(current_setlist) == len(songs):
            # Add a copy of the current setlist to our results.
            all_permutations.append(current_setlist[:])
            return

        # Recursive Step: Iterate through all songs to make a choice.
        for i in range(len(songs)):
            # If the song at index 'i' has not been used yet...
            if not used[i]:
                # --- Choose ---
                # Add the song to our current setlist and mark it as used.
                current_setlist.append(songs[i])
                used[i] = True

                # --- Explore ---
                # Recursively call the function to build the rest of the setlist.
                find_permutations(current_setlist)

                # --- Un-choose (Backtrack) ---
                # After the recursive call returns, undo our choice so we can try
                # the next song in this position.
                used[i] = False
                current_setlist.pop()

    # Start the backtracking process with an empty setlist.
    find_permutations([])
    
    return all_permutations
# Let N be the number of songs in the input list.

# Time Complexity: O(N * N!)

# There are N! (N factorial) possible permutations for a list of N unique items.

# For each of these permutations, we perform N operations to build it (appending to the list).

# This leads to a time complexity that is roughly proportional to N * N!. This is a very fast-growing complexity, which is typical for problems that explore all permutations.

# Example Usage:
must_play_songs = ["Enter Sandman", "Bohemian Rhapsody", "Stairway to Heaven"]
possible_setlists = generate_setlists(must_play_songs)

print("All possible finale setlists:")
for i, setlist in enumerate(possible_setlists):
    print(f"{i+1}: {setlist}")
# Expected: 6 different permutations.