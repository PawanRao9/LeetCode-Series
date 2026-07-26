class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return " "
        res = ""
        base = strs[0]
        for i in range(len(strs[0])):
            for word in strs[1:]:
                if i == len(word) or word[i] != base[i]:
                    return res
            res += base[i]
        return res