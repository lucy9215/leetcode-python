class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        times = []
        for hh in range(12):
            for mm in range(60):
                if (bin(hh)+bin(mm)).count('1')==num:
                    times+=['%d:%02d'%(hh,mm),]
        return times




def main():
    solution = Solution()

    a = 2

    print ('Output:', solution.readBinaryWatch(a))


if __name__ == '__main__':
    main()