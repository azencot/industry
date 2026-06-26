# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/
#
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
# Example 1:
#   Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#   Explanation: [1,3] and [2,6] overlap, merge them into [1,6].
#
# Example 2:
#   Input:  intervals = [[1,4],[4,5]]
#   Output: [[1,5]]
#   Explanation: [1,4] and [4,5] are considered overlapping (touching counts).
#
# Constraints:
#   1 <= intervals.length <= 10^4
#   intervals[i].length == 2
#   0 <= start_i <= end_i <= 10^4
#
# ---- Live-interview checklist ----
# restate -> clarify edge cases -> approach + complexity -> example -> code -> test
# Narrate invariants aloud (e.g. "intervals are sorted by start, so a new
# interval can only overlap the last one in the output").


# approach: sort intervals by start: O(n log n) time, where n is the number of intervals
# scan sorted list: if current interval ends before next: no overlap, send to ret; else, store max of end values and move to next interval: O(n) time, O(n) mem (worst case, no overalp)
# edge cases: touching overlap, nested overlap
# Overall complexity: O(n) mem, O(n log n) time; can we do better? can get rid of sort? not sure; what about mem? maybe can change in-place but it more delicate and not necessarily permitted

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        # sort intervals by start
        sorted_intervals = sorted(intervals, key=lambda l: l[0])

        # scan sorted intervals
        min_start, max_end = sorted_intervals[0][0], sorted_intervals[0][1]
        ret = []
        for interval in sorted_intervals[1:]:
            if interval[0] > max_end:               # no overlap, can store in ret
                ret.append([min_start, max_end])
                min_start, max_end = interval[0], interval[1]
            else:                                   # overlap, update max_end
                max_end = max(max_end, interval[1])

        # edge case: last interval ??
        ret.append([min_start, max_end])

        return ret




if __name__ == "__main__":
    s = Solution()

    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # expect [[1,6],[8,10],[15,18]]
    print(s.merge([[1, 4], [4, 5]]))                      # expect [[1,5]]
    print(s.merge([[1, 4], [2, 3]]))                      # expect [[1,4]] (nested)
    print(s.merge([[1, 4], [0, 4]]))                      # expect [[0,4]] (unsorted input)
    print(s.merge([[1, 4]]))                              # expect [[1,4]] (single)
