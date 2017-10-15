class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        res = [[1]]
        for i in range(1, numRows):
            res += [list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1]))]
        res = res[:numRows]
        return res


def main():
    solution = Solution()

    a = 4

    print ('Output:', solution.generate(a))

if __name__ == '__main__':
    main()