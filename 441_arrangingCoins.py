import math 

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # i = 0 
        # while i < n:
        #     n -= i
        #     i+=1
        # if n==i:
        #     return i 
        # return i - 1

        res = int(-0.5 + math.sqrt(2*n+0.25))
        return res 