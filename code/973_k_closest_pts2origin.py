# since I need the closest k -> use heap O(k * log(n))
import heapq

def kClosest(points, k):
    heap = []  # max-heap simulated via negative distances

    for x, y in points:
        dist_sq = x*x + y*y          # squared distance (no sqrt needed)

        # push (-distance, point) so the farthest of the kept points is on top
        heapq.heappush(heap, (-dist_sq, [x, y]))

        # if we have more than k points, remove the farthest one
        if len(heap) > k:
            heapq.heappop(heap)

    # extract points from heap (order doesn't matter)
    return [point for (_, point) in heap]

# import math
# 
# def kClosest(points, k):
#         """
#         :type points: List[List[int]]
#         :type k: int
#         :rtype: List[List[int]]
#         """
#         n = len(points)

#         # compute distances to origin
#         dists = [math.sqrt(x ** 2 + y ** 2) for (x,y) in points]

#         # without heap: there is a naive algorithm O(k * n)

#         # extract k min dists
#         k_closest = []
#         for i in range(k):
#                 curr_min, curr_j = float('Inf'), -1
#                 for j in range(n):
#                         if dists[j] < curr_min:
#                                 curr_min = dists[j]
#                                 curr_j = j
#                 dists[curr_j] = float('Inf')
#                 k_closest.append(points[curr_j])

#         # TODO: can this be cut to O(k * log(n)) or (n * log(k))?
        
#         # probably with a heap, but I don't get it
#         # specifically, if the heap takes O(1) to construct, how does it find
#         # next min. in O(log(n))?

#         return k_closest


print(kClosest([[1,3],[-2,2]], 1))
print(kClosest([[3,3],[5,-1],[-2,4]], 2))
