# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/

# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Fix for Optional typehint warning
from typing import Optional

# Definition for singly-linked list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution logic:
# Create solution ListNode tail. While either listnode has a valid next pointer,
# Add together both nodes' values (using 0 if one of them doesn't exist). If sum > 10,
# carry the 1 to the next sum-node. Update l1 and l2 to their next pointers.
# Do this until out of nodes. If a remaining carry exists, create a final sum-node for it
# Return first of the sum-nodes

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Set head and tail nodes
        tail = ListNode()
        head = tail

        carry = 0
        # While any nodes remain
        while l1 or l2:
            # If one of the nodes is null, set value to 0
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # _sum since sum is already in use
            _sum = v1 + v2 + carry
            carry = 1 if _sum >= 10 else 0
            # set sum to ones place of sum
            _sum = _sum % 10

            # Attach ListNode with sum to head
            head.next = ListNode(_sum)
            # Update head to that same next node
            head = head.next

            # Iterate down. If one of the nodes is null, set the next to None (null)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # If out of nodes to sum but a carry remains, manually attach a node to the head for it
        if carry == 1:
            head.next = ListNode(carry)

        # Since tail is empty, return the next pointer,
        # which is the ones' place node (i.e. l1.val + l2.val, if applicable)
        return tail.next
