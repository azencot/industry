# 3Sum: Given an integer array nums, return all distinct triplets 
# [nums[i],nums[j],nums[k]] such that i != j, i != k, j != k, and
# nums[i] + nums[j] + nums[k] = 0.
# The solution set must not contain duplicate triplets.

import numpy as np

def threeSum(nums):

	n = len(nums)
	nums = np.sort(nums)		# O(n * log(n))

	# O(n ** 2)
	for i in range(1, n-1):
		comp = -nums[i]

		l, r = i-1, i+1

		for l in range(0, i-1):
			for r in range(i+1, n)

		nums[l] + nums[r] == comp


[-1,0,1,2,-1,-4]

[-4, -1, -1, 0, 1, 2]

# def twoSum(nums, target):
# 	"""
# 	:type nums: List[int]
# 	:type target: int
# 	:rtype: List[int]
# 	"""
# 	hash = {}

# 	tuples = []
# 	for i in range(len(nums)):
# 			comp = target - nums[i]

# 			if comp in hash:
# 				tuples.append([nums[i], comp])
# 			else:
# 				hash[nums[i]] = i
# 	return tuples

# def threeSum(nums):
# 	# this is similar to 2sum, I essentially need solve many 2sum problems

# 	hash = {}

# 	threeTuples = []
# 	for i in range(len(nums)):
# 		comp = 0 - nums[i]

# 		tuples = twoSum(nums[:i] + nums[i+1:], comp)

# 		if len(tuples) > 0:
# 			for tuple in tuples:
# 				threeTuples.append([tuple[0], tuple[1], nums[i]])

# 	return set(frozenset(x) for x in threeTuples)


print(threeSum([-1,0,1,2,-1,-4]))

# Naive: iter over i,j, k -> compute sum -> check if zero -> handle reps
# n choose 3, sort per triple, construct a set

# def threeSum(nums):
	
# 	n = len(nums)

# 	tuples = set()
# 	for i in range(n):
# 		for j in range(i+1, n): 
# 			for k in range(j+1, n):
# 				if nums[i] + nums[j] + nums[k] == 0:
# 					tup = sort([nums[i], nums[j], nums[k]])
# 					tuples.add(tup)		# TODO: need to implement comparison?
# 	return tuples


