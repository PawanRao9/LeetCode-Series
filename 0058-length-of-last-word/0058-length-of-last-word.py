class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        n = len(s)
        count = 0
        l = n - 1
        while l >= 0 and s[l] != " ":
            count += 1
            l -= 1
        return count