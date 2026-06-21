# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals in the input.
import heapq

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # idea: use heapq with lex ordering of tuples?
        # insert all intervals to heap, pop (min)
        # check if overlaps with prev interval; if yes, merge, if not, split
        # complexity: O(n log n), n number of intervals
        h = []

        # O(n log n) time, O(n) mem
        for interval in intervals:
            heapq.heappush(h, interval)

        # intervals.length >= 1
        pi = heapq.heappop(h)
        ret_list = [pi]         # O(n) mem

        # O(n log n) time
        while h:
            ci = heapq.heappop(h)

            if ci[0] <= pi[1]:
                ret_list[-1][1] = max(ci[1], pi[1]) # merge intervals
            else:
                ret_list.append(ci)

            pi = ret_list[-1]

        return ret_list




