class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low, high = 0, n-1
        mini = float('inf')

        while low<=high:
            mid = (low+high)//2
            if nums[low] <= nums[mid]:
                mini = min(mini,nums[low])
                low = mid +1
            else:
                mini = min(mini, nums[mid])
                high = mid - 1
        return mini