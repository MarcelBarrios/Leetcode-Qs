# You're a software engineer at a popular music streaming service. Your next assignment is to build the backend logic for the "Trending Now" feature on the homepage. The service has a massive, real-time log of every song played by users. For the "Trending Now" list, the product manager wants to display the top K most frequently played songs over the last hour.

# A simple approach would be to count every song and then sort the entire list of unique songs by play count, but this is too slow. The list of unique songs could be in the millions, and this feature needs to be fast. You need to find a more efficient way to get just the top K songs without sorting everything.

# Your task is to write a function that takes a list of song titles (representing the play log) and an integer K, and returns a list of the K most frequent song titles.

import heapq
from collections import Counter

def get_trending_songs(songs, k):
    """
    Finds the K most frequently played songs from a list.

    This is a classic "Top K Frequent Elements" problem. The most efficient solution combines a hash map (for counting) and a min-heap (for keeping track of the top K elements).

    :param songs: A list of strings representing played songs.
    :param k: The number of top songs to return.
    :return: A list of the K most frequent song titles.
    """
    # If the input is empty, return an empty list.
    if not songs:
        return []

    # Step 1: Count the frequency of each song efficiently.
    # Counter creates a dictionary-like object: {'song_title': count}
    frequency_map = Counter(songs)

    # Step 2: Use a min-heap to keep track of the top K frequent songs.
    min_heap = []

    # Step 3: Iterate through the songs and their frequencies.
    for song, count in frequency_map.items():
        # Push a tuple of (count, song) onto the heap.
        # heapq in Python is a min-heap, so it will sort by the first item (count).
        heapq.heappush(min_heap, (count, song))
        
        # If the heap grows larger than K, remove the song with the smallest count.
        if len(min_heap) > k:
            heapq.heappop(min_heap)
            
    # Step 4: Extract the song titles from the heap to form the result.
    # The heap now contains the K songs with the highest frequencies.
    trending_list = [song for count, song in min_heap]
    
    return trending_list

# Example Usage:
play_log = ["Circles", "Blinding Lights", "Circles", "Savage Love", "Circles", "Blinding Lights", "Watermelon Sugar"]
top_k = 2
trending = get_trending_songs(play_log, top_k)
print(f"The Top {top_k} Trending Songs are: {trending}") # Expected: ['Blinding Lights', 'Circles'] (order may vary)