class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False 
        while n%3==0:
            n = n/3
        if n == 1:
            return True
        else: 
            return False 
        
#         if n<1:
#             return False
#         res = (10460353203%n == 0)
#         return res


# x = 1 
# while x<2**16:
#     x*=3

# print(x)