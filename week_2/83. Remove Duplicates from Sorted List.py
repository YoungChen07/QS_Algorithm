# Created by Young Chen at 8/26/2018
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy=ListNode(-1)
        dummy.next=head
        while dummy.next:
            if dummy.next.val == dummy.val:
                dummy.next=dummy.next.next
            else:
                dummy=dummy.next
        return head