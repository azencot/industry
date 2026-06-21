
import heapq

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    # count how many items each num in nums appear
    counts = {}

    # O(n)
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    heap = []
    for num in counts:
        heapq.heappush(heap, (counts[num],num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for (_, num) in heap]


# def topKFrequent(nums, k):
#     """
#     :type nums: List[int]
#     :type k: int
#     :rtype: List[int]
#     """

#     # count how many items each num in nums appear
#     counts = {}

#     # O(n)
#     for num in nums:
#         counts[num] = counts.get(num, 0) + 1

#     # naive algorithm: O(k * n)
#     top_k = []
#     for i in range(k):
#         curr_max = -1
#         for num in counts:
#             if counts[num] > curr_max:
#                 curr_max = counts[num]
#                 curr_num = num
#         top_k.append(curr_num)
#         counts[curr_num] = -1

#     return top_k

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1], 1))
print(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2))