# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # idea: scan the linked list, store node pointers in a dictionary, if seen, return true, if finished, return false: O(n) time, O(n) mem
        nodei, nodej = head, head

        while nodej and nodej.next and nodej.next.next:
            nodei = nodei.next
            nodej = nodej.next.next

            if nodei == nodej:
                return True

        return False
        