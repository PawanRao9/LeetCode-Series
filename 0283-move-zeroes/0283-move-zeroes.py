class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # i = 0

        # if nums[i] == 0:
        #     return

        # while i < n :
        #     if i == 0:
        #         break

        # if i == len(nums):
        #     return

        # j = i+1
        # while j < n:
        #     if nums[j] != 0:
        #         nums[i], nums[j] = nums[j], nums[i]
        #         i +=1
        #     j +=1
        n = len(nums)
        last_zero = 0
        for i in range(0,n):
            if nums[i] != 0:
                nums[last_zero], nums[i] = nums[i], nums[last_zero]
                last_zero += 1