# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you 
# have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

import heapq

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # naive O(n ** 2) time with O(1) additional mem
        # heap: O(n log n) time with O(n) additional mem
        # wait = [0] * len(temperatures)

        # h = []
        # heapq.heappush(h, [temperatures[0], 0])
        # for idx, temp in enumerate(temperatures[1:], start=1):
        #     while len(h) > 0 and h[0][0] < temp:
        #         prev_temp, prev_idx = heapq.heappop(h)
        #         wait[prev_idx] = idx - prev_idx

        #     heapq.heappush(h, [temp, idx])
                
        # return wait

        # list: O(n) time with O(n) additional mem (worst case)
        wait = [0] * len(temperatures)

        idx_todo = []
        for idx, temp in enumerate(temperatures):
            
            while len(idx_todo) > 0 and temperatures[idx_todo[-1]] < temp:
                wait[idx_todo[-1]] = idx - idx_todo[-1]
                idx_todo.pop()

            idx_todo.append(idx)

        return wait


sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))