class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        seen = set()
        n = len(grid)
        repeated = -1 

        for row in grid:
            for num in row :
                if num in seen:
                    repeated = num
                seen.add(num)
        missing = -1

        for num in range(1, n * n + 1):
            if num not in seen:
                missing = num
                break
        return [repeated, missing]