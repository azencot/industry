def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        
        for i in range(len(nums)):
                comp = target - nums[i]

                if comp in hash:
                        return [i, hash[comp]]
                else:
                        hash[nums[i]] = i

# def twoSum(nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         n = len(nums)

#         for i in range(n):
#                 for j in range(i+1, n):
#                         if nums[i] + nums[j] == target:
#                                 return [i, j]

print(twoSum([2,7,11,15], 9))
print(twoSum([3,2,4], 6))
print(twoSum([3,3], 6))