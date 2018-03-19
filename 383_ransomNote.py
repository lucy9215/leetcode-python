import collections

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        res = collections.Counter(ransomNote) - collections.Counter(magazine)
        return not res #(res == collections.Counter())



def main():
    solution = Solution()

    a = "bcjefgecdabaa"
    b = "hfebdiicigfjahdddiahdajhaidbdgjihdbhgfbbccfdfggdcacccaebh"

    print ('Output:', solution.canConstruct(a,b))


if __name__ == '__main__':
    main()