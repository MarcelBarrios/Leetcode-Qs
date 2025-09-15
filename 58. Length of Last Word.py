# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        The most straightforward approach is to first clean up the input string and then isolate
        the last word and get its length.
        """
        # removes all leading (at the beginning) and trailing (at the end) whitespace from a string.
        # O(n)
        trimmed_s = s.strip()
        
        # breaks a string up into a list of smaller strings, using the space character as the delimiter. 
        # It also handles multiple spaces between words gracefully.
        # O(n)
        words = trimmed_s.split(' ')
        
        # This line uses Python's list indexing to get an element from the words list. 
        # Using [-1] is a convenient shorthand to get the very last element in a list.
        last_word = words[-1]
        
        # The built-in len() function takes a string (or a list) and returns the number of characters in it.
        return len(last_word)
    # O(n)