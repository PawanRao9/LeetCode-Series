class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == "":
            return 0

        n = len(needle)
        m = len(haystack)
        for i in range(m - n + 1):
            match = True
            for j in range(n):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            
            if match:
                return i
        return -1