# Created by Young Chen at 8/26/2018

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        first=dummy
        second=dummy
        while n>=0 :
            first=first.next
            n=n-1
        while first is not None:
            first=first.next
            second=second.next
        second.next=second.next.next
        return dummy.next