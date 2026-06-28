"""
57. Insert Interval
https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals where intervals[i] = [start_i, end_i]
represents the start and the end of the ith interval and intervals is sorted in ascending
order by start_i. You are also given an interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by
start_i and intervals still does not have any overlapping intervals. Merge overlapping
intervals if necessary.

Return intervals after the insertion.

Example 1:
    Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
    Output: [[1,5],[6,9]]

Example 2:
    Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
    Output: [[1,2],[3,10],[12,16]]

Example 3:
    Input: intervals = [], newInterval = [5,7]
    Output: [[5,7]]

Constraints:
    0 <= len(intervals) <= 10**4
    intervals[i].length == 2
    newInterval.length == 2
    0 <= start_i <= end_i <= 10**5
    intervals is sorted by start_i and non-overlapping
"""

# "I'll scan once in three phases: add intervals that end before newInterval starts; merge all overlapping intervals into newInterval; then add the rest."

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        ret = []
        i, n = 0, len(intervals)
        start, end = newInterval
        
        while i < n and intervals[i][1] < start:
            ret.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        ret.append([start, end])
        
        while i < n:
            ret.append(intervals[i])
            i += 1     
        

        return ret
        


if __name__ == "__main__":
    sol = Solution()

    assert sol.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert sol.insert([], [5, 7]) == [[5, 7]]
    assert sol.insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert sol.insert([[3, 5], [7, 9]], [1, 2]) == [[1, 2], [3, 5], [7, 9]]
    assert sol.insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert sol.insert([[1, 5]], [0, 6]) == [[0, 6]]

    print("all tests passed")
