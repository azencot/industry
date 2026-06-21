def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    print(nums)
    
    n = len(nums)
    
    if n == 0:
        return 0

    ret = 0
    
    if sum(nums) == k:
        ret = 1

    return ret + subarraySum(nums[1:], k) + subarraySum(nums[:n-1], k)

print(subarraySum([1, 1, 1], 2))
print(subarraySum([1, 2, 3], 3))
print(subarraySum([1, 2, 1, 2], 3))