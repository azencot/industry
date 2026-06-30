# LeetCode 57. Insert Interval
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [start_i, end_i] represent the start and the end of the
# ith interval and intervals is sorted in ascending order by start_i.
# You are also given an interval newInterval = [start, end] that represents
# the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by start_i and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.
#
# You may assume that intervals is sorted by start_i in ascending order.
#
# Example 1:
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
# Example 2:
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#
# Constraints:
# 0 <= len(intervals) <= 10^4
# intervals[i].length == 2
# 0 <= start_i <= end_i <= 10^5
# intervals is sorted by start_i in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
#
# LeetCode: https://leetcode.com/problems/insert-interval/

# approach: scan intervals in three phases: 1) interval in intervals finishes before newInterval begins: add to ret; 2) overlapping intervals that need merge; 3) post intervals
# complexity: O(n) time (a single scan); O(n) mem (create new ret)

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        i, n = 0, len(intervals)
        start, end = newInterval[0], newInterval[1]

        ret = []
        
        # phase 1: interval in intervals finishes before newInterval
        while i < n and intervals[i][1] < start:
            ret.append(intervals[i])
            i += 1

        # phase 2: interval in intervals overlaps with newInterval
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        ret.append([start, end])

        # phase 3: interval in intervals starts after newInterval
        while i < n:
            ret.append(intervals[i])
            i += 1
        
        return ret


if __name__ == "__main__":
    solution = Solution()
    print(solution.insert([[1, 3], [6, 9]], [2, 5]))  # [[1,5],[6,9]]
    print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))  # [[1,2],[3,10],[12,16]]
    print(solution.insert([], [5, 7]))  # [[5,7]]
    print(solution.insert([[1, 5]], [2, 3]))  # [[1,5]]
