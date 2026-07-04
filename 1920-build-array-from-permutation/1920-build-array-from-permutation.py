class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        r = []
        for i in range(0,n):
            r.append(nums[nums[i]])
        return r