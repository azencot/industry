# Given the head of a singly linked list, reverse the list, and return 
# the reversed list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # idea: traverse the list while creating a new one with reversed links
        # complexity: O(n) mem and O(n) time
        # save mem by using the same list? it is like "swap"
        next, node = None, head

        while node is not None:
            # revert edge
            tmp_node = node.next
            node.next = next
            
            # continue forward traversal
            next = node
            node = tmp_node

        return next