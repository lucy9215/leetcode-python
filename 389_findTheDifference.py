import collections 
class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_ref = collections.Counter(s)
        t_ref = collections.Counter(t)
        res = ''.join((t_ref - s_ref).keys())
        return res




def main():
    solution = Solution()

    a = 'abcd'
    b = 'abcddd'

    print ('Output:', solution.findTheDifference(a,b))


if __name__ == '__main__':
    main()