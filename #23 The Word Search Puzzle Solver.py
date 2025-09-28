def solve_word_search(board, word):
    """
    Determines if a word can be found in a 2D grid of characters.

    This problem asks us to find a path in the grid that spells out the word. Since we don't know where the word might start, and we have the constraint of not reusing cells, this is a classic application for backtracking, implemented with a Depth-First Search (DFS).

    The overall strategy is to scan every cell of the grid. If a cell matches the first letter of our word, we will launch a deeper search from that cell to see if we can find the rest of the word.

    :param board: A 2D list of characters.
    :param word: The string word to search for.
    :return: True if the word is found, False otherwise.
    """
    rows, cols = len(board), len(board[0])

    def search(row, col, index):
        """
        A recursive backtracking function to find the word path.
        :param index: The index of the character in 'word' we are currently searching for.
        """
        # Base Case 1: Failure (out of bounds or wrong character).
        if not (0 <= row < rows and 0 <= col < cols and board[row][col] == word[index]):
            return False

        # Base Case 2: Success! We've found all the letters.
        if index == len(word) - 1:
            return True

        # --- Action: Mark the current path ---
        # Temporarily change the character to prevent reusing it in this same path.
        original_char = board[row][col]
        board[row][col] = '#'
        
        # --- Recurse: Explore neighbors ---
        # Check all four directions for the next letter.
        found = (search(row + 1, col, index + 1) or
                 search(row - 1, col, index + 1) or
                 search(row, col + 1, index + 1) or
                 search(row, col - 1, index + 1))
        
        # --- Backtrack: Un-mark the path ---
        # Restore the original character so it can be used in other potential paths.
        board[row][col] = original_char
        
        return found

    # Main loop to start a search from every cell on the board.
    for r in range(rows):
        for c in range(cols):
            # We only need to start a search if the cell matches the first letter.
            if board[r][c] == word[0]:
                if search(r, c, 0):
                    return True
    
    # If we loop through the entire board and find nothing, the word doesn't exist.
    return False
# Let R be the number of rows, C be the number of columns, and L be the length of the word.

# Time Complexity: O(R * C * 3^L)

# In the worst case, we might initiate a DFS search from every cell (R * C).

# The DFS search itself can branch out. At each step, we explore up to 4 neighbors. However, since we can't go back to the cell we just came from, it's more like 3 branches at each step. This can go on for a depth of L.

# This gives a rough upper bound. In practice, it's much faster because many paths are pruned early if the letters don't match.

# Example Usage:
game_board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word_to_find = "SEE"
print(f"Can the word '{word_to_find}' be found? {solve_word_search(game_board, word_to_find)}") # Expected: True

word_to_find_2 = "ABCB"
print(f"Can the word '{word_to_find_2}' be found? {solve_word_search(game_board, word_to_find_2)}") # Expected: False (can't reuse 'B')