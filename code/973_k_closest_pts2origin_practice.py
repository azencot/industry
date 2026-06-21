# Given an array of points where points[i] = [xi, yi] represents a point 
# on the X-Y plane and an integer k, return the k closest points to the 
# origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean 
# distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be 
# unique (except for the order that it is in).
import heapq

class Solution(object):
    def kClosest(self, points, k):
        # # this solution targets worst case scenarios;

        # # sort by distance
        # points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])

        # # return first k
        # return points[:k]

        # with heap, i might not need to pay the O(n log n), but O(n log k)
        h = []

        for x, y in points:
            dist = x*x + y*y

            heapq.heappush(h, (-dist, x, y))

            if len(h) > k:
                heapq.heappop(h)

        return [[x, y] for [_, x, y] in h]

