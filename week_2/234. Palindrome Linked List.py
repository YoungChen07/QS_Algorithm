# Created by Young Chen at 8/26/2018
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        stack = []
        dummy = head
        while dummy:
            stack.append(dummy)
            dummy = dummy.next
        while head:
            if head.val != stack.pop().val:
                return False
            head = head.next
        return True
