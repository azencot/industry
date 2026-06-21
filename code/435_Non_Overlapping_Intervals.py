# Given an array of intervals intervals where intervals[i] = [starti, endi], return 
# the minimum number of intervals you need to remove to make the rest of the intervals 
# non-overlapping.

# Note that intervals which only touch at a point are non-overlapping. For example, 
# [1, 2] and [2, 3] are non-overlapping.

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        # idea: store hash of intervals at their intersection (costly?)

        # once I have this representation, find intervals with most intersections, remove it, iterate, until all intervals are non-overlapping

        # say i have two intervals [si, ei] and [sj, ej], they overlap if
        # [si, ei] \subset [sj, ej] if sj <= ei < ej or sj <= si < ej

        # tree structure? a node is connected in edges to intervals it overlaps with
        # start by removing nodes whose indeg is highest

        # how to find these nodes efficiently? how to construct rep. efficiently?

        # naive: O(n ** 2) where n is the number of intervals
        # if we sort by start: can lower to O(n log n): sort by start and a single pass

        # can decision be local? i.e., sort, and decide along the scan
        # for instance, say I am at an intervals which intersects with another
        # but the other intervals intersects with two

     