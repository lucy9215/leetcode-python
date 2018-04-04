class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        res = bin(x^y).count('1')
        return res 

def main():
    solution = Solution()

    a = 1
    b = 4

    print ('Output:', solution.hammingDistance(a,b))


if __name__ == '__main__':
    main()