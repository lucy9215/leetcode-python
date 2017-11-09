class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # it is a fibonacci
        if n<=0:
            return 0 
        a = b = 1
        for i in range(n):
            a, b = b, a+b
        # return a fibonacci(1,1,2,3,5...) indexed from 0, and return 0 when idex is 0. 
        # i.e return a fibonacci(1,2,3,5...) indexed from 1. 
        return a 


def main():
    solution = Solution()

    a = 1

    print ('Output:', solution.climbStairs(a))


if __name__ == '__main__':
    main()