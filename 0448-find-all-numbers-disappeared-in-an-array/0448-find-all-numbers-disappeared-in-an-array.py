class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        
        duplicate = []
        missing = []
        seen = set()

        for num in nums:
            if num in seen:
                duplicate.append(num)
            else:
                seen.add(num)
        
        for i in range(1,n+1):
            if i not in seen:
                missing.append(i)

        return missing