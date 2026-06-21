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