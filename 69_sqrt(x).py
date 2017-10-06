# import math

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # return int(np.sqrt(x))

        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return int(r)


def main():
    solution = Solution()
    a = 4
    print ('Output:', solution.mySqrt(a))


if __name__ == '__main__':
    main()