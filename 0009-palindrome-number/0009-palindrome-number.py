class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # x = str(x)
        # left = x[0]
        # right = len(x) - 1
        # while left < right:
        #     if x[left] != x[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # return True

        # result = 0
        # num =  x
        # while num > 0:
        #     last_digit = num % 10
        #     result = (result * 10) + last_digit
        #     num = num // 10
        # if result == x:
        #     return True
        # return False
        re = False
        y = str(x)
        
        if y == y[::-1]:
            re = True
        return re