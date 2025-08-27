# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        use a list as our stack. The plan is to iterate through the string and 
        use the stack to keep track of the opening brackets we're waiting to close.
        """
        # A stack to keep track of opening brackets.
        stack = []

        # A mapping of closing brackets to their corresponding opening brackets.
        bracket_map = {")": "(", "}": "{", "]": "["}

        # Iterate through each character in the string.
        for char in s:
            # If the character is a closing bracket.
            if char in bracket_map:
                # Pop the top element from the stack if it's not empty;
                # otherwise, assign a dummy value that won't match.
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the expected opening bracket,
                # the string is invalid.
                if bracket_map[char] != top_element:
                    return False
            # If it's an opening bracket, push it onto the stack.
            else:
                stack.append(char)
        
        # A valid string will result in an empty stack at the end.
        return not stack