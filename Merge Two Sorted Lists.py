# https://leetcode.com/problems/merge-two-sorted-lists/description/

# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]

        The main idea is that we are building a new, sorted list by picking the smallest available
        node from either list1 or list2 at each step.
        """
        # Create a dummy node to serve as the head of the new list.
        dummy = ListNode()
        # 'current' will be used to build the new list.
        current = dummy

        # Loop as long as both lists have nodes.
        # O(m + n)
        while list1 and list2:
            # Compare the values of the two lists' current nodes.
            if list1.val <= list2.val:
                # If list1's node is smaller, append it and move list1's pointer.
                current.next = list1
                list1 = list1.next
            else:
                # If list2's node is smaller, append it and move list2's pointer.
                current.next = list2
                list2 = list2.next
            
            # Move the 'current' pointer forward to the new last node.
            current = current.next

        # After the loop, one of the lists might have remaining nodes.
        # Append the non-empty list to the end of the merged list.
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        # The merged list starts at the node after the dummy head.
        return dummy.next
    
    # O(m + n)