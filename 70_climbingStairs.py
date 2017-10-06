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
        return a 


def main():
    solution = Solution()

    a = 4

    print ('Output:', solution.climbStairs(a))


if __name__ == '__main__':
    main()