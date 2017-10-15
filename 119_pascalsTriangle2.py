class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(0, rowIndex):
            res = list(map(lambda x, y: x+y, res + [0], [0] + res))
        return res


def main():
    solution = Solution()

    a = 1

    print ('Output:', solution.getRow(a))

if __name__ == '__main__':
    main()