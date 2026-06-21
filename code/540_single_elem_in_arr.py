def singleNonDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    while nums:
        print(nums)
        n = len(nums)

        if n == 1:
            return nums[0]

        idx = n // 2

        # edge case: uniq at the middle
        if nums[idx] != nums[idx-1] and nums[idx] != nums[idx + 1]:
            return nums[idx]

        # left rest is odd
        if len(nums[:idx]) % 2 == 1:
            if nums[idx] == nums[idx - 1]:
                nums = nums[idx+1:]
            else:
                nums = nums[:idx]

        # left rest is even
        else:
            if nums[idx] == nums[idx - 1]:
                nums = nums[:idx-1]
            else:
                nums = nums[idx+2:]

# print(singleNonDuplicate(None, [1,1,2,3,3,4,4,8,8]))
print(singleNonDuplicate(None, [1,1,2,2,3]))
