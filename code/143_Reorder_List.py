# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # 1: find list length n: O(n) time, O(1) mem
        n, curr_head = 0, head
        while curr_head:
            n += 1
            curr_head = curr_head.next
        

        # 2: scan list, after half (if n even) or half+1 (if n odd): switch next to prev (reverse the second half of list); mark half or half+1 next to be None for stopping
        if n % 2 == 0:
            i = n // 2
        else:
            i = n // 2 + 1

        j, curr_mid = 0, head
        while curr_mid:
            j += 1
            if j == i:
                break

            curr_mid = curr_mid.next

        curr_head = curr_mid.next
        curr_mid.next = None

        curr_prev, curr_next = None, None
        while curr_head:
            curr_next = curr_head.next
            
            curr_head.next = curr_prev
            curr_prev = curr_head
            curr_head = curr_next
        tail = curr_prev

        # 3: head and tail iterators: increment both (head and then tail), and re-order, i.e., put head and then tail; important: don't mess next links, so first increment but keep links to previous nodes
        curr_head, curr_tail = head, tail
        while curr_tail:
            next_head = curr_head.next
            next_tail = curr_tail.next

            curr_head.next = curr_tail
            curr_tail.next = next_head

            curr_head = next_head
            curr_tail = next_tail