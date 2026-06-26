# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
#
# Example 1:
#   Input:  nums = [1,1,1,2,2,3], k = 2
#   Output: [1,2]
#
# Example 2:
#   Input:  nums = [1], k = 1
#   Output: [1]
#
# Constraints:
#   1 <= nums.length <= 10^5
#   -10^4 <= nums[i] <= 10^4
#   k is in the range [1, number of unique elements in nums]
#   The answer is guaranteed to be unique.
#
# Follow-up: better than O(n log n), where n = array length.
#
# ---- Live-interview checklist ----
# restate -> clarify edge cases -> approach + complexity -> example -> code -> test
# Narrate invariants aloud (e.g. "heap holds the k highest-frequency items so far").


# since better than O(n log n) is required, it seems like we need a heap of size k, then we will get O(n log k)
# however, what happens with items I eliminate? how do they get back?
# perhaps first maintain a dict of appearances O(n) mem + time
# then create a heap of size k: O(n log k) time + O(k) mem
# overall: O(n + k) = O(n) mem and O(n + n log k) = O(n log k) time
import heapq 

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        # create a dict of occurances (O(n) mem + time)
        occur = {}
        for num in nums:
            occur[num] = occur.get(num, 0) + 1      # heap keeps min at the top

        # create a heap of size k
        h = []
        for num in occur:
            heapq.heappush(h, (occur[num], num))        # lex order will keep correct ordering

            if len(h) > k:
                heapq.heappop(h)                        # greedy: remove least frequent item


        ret = [num for _, num in h]
        return ret

if __name__ == "__main__":
    s = Solution()

    # Order may vary; compare as sets.
    print(sorted(s.topKFrequent([1, 1, 1, 2, 2, 3], 2)))  # expect [1, 2]
    print(sorted(s.topKFrequent([1], 1)))                  # expect [1]
    print(sorted(s.topKFrequent([4, 4, 4, 5, 5, 6], 1)))   # expect [4]
    print(sorted(s.topKFrequent([1, 2, 3], 3)))            # expect [1, 2, 3]
