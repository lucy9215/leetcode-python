class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        offset = ord('A') - 1 
        num = 0 
        i = 0 
        for v in s[::-1]:
            num += (ord(v) - offset)*26**(i)
            i+=1
        return num



def main():
    solution = Solution()

    a = 'A'

    print ('Output:', solution.titleToNumber(a))


if __name__ == '__main__':
    main()


