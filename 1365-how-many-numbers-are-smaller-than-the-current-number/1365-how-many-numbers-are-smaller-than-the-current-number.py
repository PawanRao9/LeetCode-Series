class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        new_arr = []
        for i in range(0,n):
            count = 0
            for j in range(0,n):
                if (nums[i]>nums[j]):
                    count += 1
            new_arr.append(count)
        return new_arr