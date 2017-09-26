class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lndl = len(needle)
        lpath = len(haystack) - lndl + 1
        for i in range(lpath):
            if needle == haystack[i:i+lndl]:
                return i
        return -1


def main():
    solution = Solution()

    haystack = 'helloluxiwhat'
    needle = 'luxi'

    print ('Output:', solution.strStr(haystack,needle))


if __name__ == '__main__':
    main()