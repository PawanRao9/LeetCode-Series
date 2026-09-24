class Solution(object):

    def smallestIndex(self, nums):
        n = len(nums)

        for i in range(n):
            num = nums[i]
            summ = 0

            while num > 0:
                summ = summ + num % 10
                num = num // 10

            if summ == i:
                return i

        return -1