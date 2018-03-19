import collections 

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        ref = collections.Counter(s)
        for i,v in enumerate(s):
            if ref[v]==1:
                return i 
        return -1


def main():
    solution = Solution()

    a = "loveleetcode"

    print ('Output:', solution.firstUniqChar(a))


if __name__ == '__main__':
    main()