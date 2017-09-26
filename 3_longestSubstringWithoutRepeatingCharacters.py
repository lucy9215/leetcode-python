class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        pocket = {}
        start = 0 
        max_str = 0 
        for i,v in enumerate(s):
            if v in pocket:
                start = max(pocket[v] +1 , start) 
            max_str = max((i - start + 1),max_str) 
            pocket[v] = i 
        return max_str 




def main():
    solution = Solution()
    # s = 'aaaaaaa'
    s = 'a'
    s = 'dddvdf'
    # s = 'abnnfpdmpi'
    # s = 'abcdef'
    print ('Output:', solution.lengthOfLongestSubstring(s))


if __name__ == '__main__':
    main()