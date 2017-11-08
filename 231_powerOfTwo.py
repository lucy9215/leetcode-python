class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n ==1:
            return True
        elif n<1:
            return False
        while n:
            if n==2:
                return True
            elif n%2 != 0:
                return False
            else:
                n = n/2


def main():
    solution = Solution()

    a = 2  

    print ('Output:', solution.isPowerOfTwo(a))


if __name__ == '__main__':
    main()