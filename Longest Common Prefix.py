# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

class Solution(object):
    def longestCommonPrefix(self, strs):        
        strs_length = len(strs[0])
        # Store the length of the first string as our maximum possible prefix length
        
        if len(strs) == 1:
        # Check if the array contains only one string
            return strs[0]
            # If only one string exists, return it as the longest common prefix
        
        for i in range(strs_length):
        # Loop from 0 to (length of first string - 1)
        # This will try prefixes of decreasing length: full string, then one char less, etc.
        
            for_check = strs[0][:(strs_length-i)]
            # Create a candidate prefix by taking characters from start of first string
            # Length = (original_length - current_iteration)
            # i=0: take full string, i=1: take all but last char, i=2: take all but last 2 chars, etc.
            
            is_good = all(s.startswith(for_check) for s in strs)
            # Check if ALL strings in the array start with the current candidate prefix
            # all() returns True only if every string starts with for_check
            
            if is_good:
            # If the current candidate prefix is found in all strings
                return for_check
                # PSEUDOCODE: Return this prefix (it's the longest one that works)
        
        return ""
        # If no common prefix found after trying all possibilities, return empty string