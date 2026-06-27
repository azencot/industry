# 19. Remove Nth Node From End of List
#
# Given the head of a linked list, remove the nth node from the end of the list
# and return its head.
#
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
# Example 2:
# Input: head = [1], n = 1
# Output: []
#
# Example 3:
# Input: head = [1,2], n = 1
# Output: [1]
#
# Constraints:
# - The number of nodes in the list is sz.
# - 1 <= sz <= 30
# - 0 <= Node.val <= 100
# - 1 <= n <= sz
#
# Follow up: Could you do this in one pass?
# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# approach: slow/fast iterators (i | i+n); does the work in a single pass; O(1) mem and O(L) time

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
        # init iterators to (i|i+n)
        dummy = ListNode(0, head)
        node1, node2 = dummy, head
        for _ in range(n):
            node2 = node2.next

        # scan
        while node2 != None:
            node1 = node1.next
            node2 = node2.next

        # remove node
        node1.next = node1.next.next

        return dummy.next


def build_list(values):
    dummy = ListNode()
    curr = dummy
    for value in values:
        curr.next = ListNode(value)
        curr = curr.next
    return dummy.next


def to_list(head):
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next
    return values


if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
    ]

    sol = Solution()
    for values, n, expected in tests:
        result = to_list(sol.removeNthFromEnd(build_list(values), n))
        print(values, n, result, "PASS" if result == expected else "FAIL")
