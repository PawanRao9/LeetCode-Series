class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # n = len(nums)
        
        # duplicate = []
        # missing = []
        # seen = set()

        # for num in nums:
        #     if num in seen:
        #         duplicate.append(num)
        #     else:
        #         seen.add(num)
        
        # for i in range(1,n+1):
        #     if i not in seen:
        #         missing.append(i)

        # return missing

        n = len(nums)

        # freq = [0] *(n + 1)
        # for num in nums:
        #     freq[num] +=1
        
        # duplicte = []
        # missing = []

        # for i in range(1,n+1):
        #     if freq[i] == 0:
        #         missing.append(i)
        #     # elif freq[i] > 1:
        #     #     duplicate.append(i)
        # return missing

        num_set = set(nums)
        ans = []
        for i in range(1, n+1):
            if i not in num_set:
                ans.append(i)
        return ans