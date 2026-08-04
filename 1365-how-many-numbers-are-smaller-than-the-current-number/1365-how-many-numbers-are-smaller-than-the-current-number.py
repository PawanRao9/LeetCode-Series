class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # n = len(nums)
        # new_arr = []
        # for i in range(0,n):
        #     count = 0
        #     for j in range(0,n):
        #         if (nums[i]>nums[j]):
        #             count += 1
        #     new_arr.append(count)
        # return new_arr
        freq = [0] * 101

        # Count frequencies
        for num in nums:
            freq[num] += 1

        # Prefix sum
        for i in range(1, 101):
            freq[i] += freq[i - 1]

        ans = []

        # Build answer
        for num in nums:
            if num == 0:
                ans.append(0)
            else:
                ans.append(freq[num - 1])
        return ans