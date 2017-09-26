class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        if len(s)>0:
            return len(s[-1])
        else :
            return 0 



def main():
    solution = Solution()

    s = 'jkfldsj jdsi dd'
    # s = ''

    print ('Output:', solution.lengthOfLastWord(s))

if __name__ == '__main__':
    main()
