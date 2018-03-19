import collections 

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = collections.Counter(s)
        r = 0 
        l = 0 
        for key in dic.keys():
            if r == 0:
                r = dic[key]%2
            l += (dic[key]//2)*2
        l+=r 
        return l 



def main():
    solution = Solution()

    a = 'abccccdd'

    print ('Output:', solution.longestPalindrome(a))


if __name__ == '__main__':
    main()