# 28. Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.
 
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # Get the lengths of the two strings.
        n = len(haystack)
        m = len(needle)

        # Loop through the haystack, but stop when the remaining
        # part of the haystack is shorter than the needle.
        # O(n)
        for i in range(n - m + 1):
            # Check if the slice of the haystack starting at index 'i'
            # with the length of the needle matches the needle.
            # O(m)
            if haystack[i:i+m] == needle:
                # If a match is found, return the starting index.
                return i
        
        # If the loop completes without finding a match, return -1.
        return -1
# O(n m)