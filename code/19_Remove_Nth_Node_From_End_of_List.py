# Given the head of a linked list, remove the nth node from the end of the list 
# and return its head.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """

        # switch direction going to tail
        # switch direction going to head
        # remove nth
        # O(n) time, O(1) mem

        # scan, find list length, keep pointer to nth node
        # O(n) time, O(n) mem

        # better: keep two iterators with lag n between them; when the more faster iterator gets to end of list, the slower iterator removes node O(1) mem and O(n) time


        