class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # h = {}
        # for i, num in enumerate(nums):
        #     comp = target - num
        #     if comp in h:
        #         return [h[comp],i]
        #     h[num] = i

        hasi = {}
        for i, num in enumerate(nums):
            x = target - num
            if x in hasi:
                return [hasi[x],i]
            hasi[num] = i