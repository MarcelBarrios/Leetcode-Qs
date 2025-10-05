# Before smartphones and touchscreens, mobile phones had keypads where each number key from 2 to 9 
# corresponded to a set of letters. To type a word, you would press a key multiple times. Now, imagine 
# you are a software engineer in the early 2000s tasked with creating a feature that generates all
#  possible "words" that could be formed from a sequence of key presses.

# For example, on a standard T9 keypad, the number 2 maps to ['a', 'b', 'c'] and 3 maps to ['d', 'e', 'f'].
# If a user types the digits "23", your program should generate a list of all possible two-letter combinations,
# such as "ad", "ae", "af", "bd", "be", "bf", and so on.

# Your task is to write a program that takes a string of digits (from 2-9) and returns a list of all possible
# letter combinations that the number could represent.

def generate_t9_combinations(digits):
    """
    The core idea is to build the combination one character at a time. We'll make a choice for the first 
    digit, then recursively handle the rest of the digits. Once that recursive path is fully explored, 
    we "backtrack" and try the next choice for the first digit.

    :param digits: A string containing digits from '2' to '9'.
    :return: A list of all possible letter combinations.
    """
    # Handle the edge case of an empty input string.
    if not digits:
        return []

    # A mapping from digits to their corresponding letters on a T9 keypad.
    keypad_map = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }

    # The list to store our final results.
    results = []

    def backtrack(index, current_combination):
        """
        A recursive helper function to explore all combinations.
        :param index: The current digit index we are processing.
        :param current_combination: The string built so far.
        """
        # Base Case: If we've processed all digits, we have a complete combination.
        if index == len(digits):
            results.append(current_combination)
            return

        # Recursive Step: Explore choices for the current digit.
        current_digit = digits[index]
        possible_letters = keypad_map[current_digit]

        # Loop through each possible letter for the current digit.
        for letter in possible_letters:
            # Make a choice (append the letter) and explore deeper.
            backtrack(index + 1, current_combination + letter)
            # Backtracking happens implicitly when this recursive call returns,
            # and the loop proceeds to the next letter.

    # Start the backtracking process from the first digit (index 0) with an empty string.
    backtrack(0, "")
    
    return results
# Time Complexity: O(N * M^N)

# The number of possible combinations is roughly M^N in the worst case.

# For each of these combinations, we are performing operations (like string concatenation) that take O(N) time to build the final string.

# This gives us a total time complexity proportional to the number of combinations multiplied by the length of each combination.

# Example Usage:
input_digits = "23"
combinations = generate_t9_combinations(input_digits)
print(f"Combinations for '{input_digits}': {combinations}")
# Expected: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

input_digits_2 = "7"
combinations_2 = generate_t9_combinations(input_digits_2)
print(f"Combinations for '{input_digits_2}': {combinations_2}")
# Expected: ['p', 'q', 'r', 's']

# Solution 2

from collections import deque

def generate_t9_combinations_iterative(digits):
    """
    Generates all possible letter combinations for a given string of T9 digits using an iterative queue.

    :param digits: A string containing digits from '2' to '9'.
    :return: A list of all possible letter combinations.
    """
    # Handle the edge case of an empty input string.
    if not digits:
        return []

    # A mapping from digits to their corresponding letters on a T9 keypad.
    keypad_map = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }

    # Initialize a queue with an empty string as the starting point.
    # A deque is efficient for adding and removing from both ends.
    queue = deque([""])

    # Iterate through each digit in the input string.
    for digit in digits:
        # Get the number of partial combinations currently in the queue.
        # We only want to process the combinations from the previous level.
        level_size = len(queue)
        
        # Process each of the existing partial combinations.
        for _ in range(level_size):
            # Remove a partial combination from the front of the queue.
            partial_combination = queue.popleft()

            # Get the letters for the current digit.
            possible_letters = keypad_map[digit]

            # Create new combinations by appending each possible letter
            # and add them to the back of the queue.
            for letter in possible_letters:
                queue.append(partial_combination + letter)

    # After all digits are processed, the queue contains all full combinations.
    return list(queue)
# Let N be the length of the input digits string, and M be the maximum number of letters a digit can map to (which is 4).

# Time Complexity: O(N * M^N)

# The nested loops effectively build up to M^N combinations. The string concatenations inside the loop contribute the N factor, as each final string has length N.

# Example Usage:
input_digits = "23"
combinations = generate_t9_combinations_iterative(input_digits)
print(f"Iterative combinations for '{input_digits}': {combinations}")
# Expected: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']