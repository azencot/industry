# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and 
# intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another 
# interval.

# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping 
# intervals (merge overlapping intervals if necessary).

# Return intervals after the insertion.

# Note that you don't need to modify intervals in-place. You can make a new array and return it.
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        start, end = newInterval[0], newInterval[1]

        # find i, j; all intervals in [i, j] need merging
        n = len(intervals)
        i, j, need_merge = 0, n - 1, False
        for k in range(n):
            if intervals[k][0] > start:     # need previous k
                i = k - 1       # get -1 if k == 0

            if intervals[k][0] > end

            if intervals[k][0] <= start and start <= intervals[k][1]:
                i = k

        # construct intervals2 with merging if needed: O(n) time and O(n) mem
        # merge if needed
        if need_merge:
            merged = []
            for k in range(i, j):
                if intervals[k][0] == start and intervals[k][1] > end or intervals[k][0] > start:
                    merged.append(newInterval)

                merged.append(intervals[k])
        else:
            merged = [newInterval]

        return intervals[:i] + merged + intervals[j:]       # O(n) time + O(n) memory

        

        