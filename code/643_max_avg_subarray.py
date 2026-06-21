
# one single pass over nums: time O(n); space O(1)
# rolling window: track current mean and max mean
def findMaxAverage(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        
        max_sum = sum(nums[0:k])

        curr_sum = max_sum

        for i in range(1, n-k+1):
                curr_sum = (curr_sum - nums[i-1] + nums[i+k-1])

                print(curr_sum)

                if curr_sum > max_sum:
                        max_sum = curr_sum

        return float(max_sum) / k


print(findMaxAverage([1,12,-5,-6,50,3], 4))
# print(findMaxAverage([5], 1))