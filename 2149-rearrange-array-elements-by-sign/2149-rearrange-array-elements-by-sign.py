class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        p_index,n_index = 0,1
        result = [0] * n
        for i in range(0,n):
            if nums[i] >= 0:
                result[p_index] = nums[i]
                p_index += 2
            else:
                result[n_index] = nums[i]
                n_index += 2
        return result