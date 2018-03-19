class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        if b == 0: 
            return a if a <= MAX else ~(a ^ mask)
        else:
            double_identical_bits =  self.getSum((a ^ b) & mask, ((a & b) << 1) & mask)
            return double_identical_bits


def main():
    solution = Solution()

    a = 5 
    b = 6


    print ('Output:', solution.getSum(a,b))


if __name__ == '__main__':
    main()