class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        ordered_map = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        summ = 0 
        lens = len(s)
        for i,v in enumerate(s[:-1]):
            if i+1<lens and ordered_map[v]<ordered_map[s[i+1]]:
                summ -= ordered_map[v]
            else:
                summ += ordered_map[v]
        return summ + ordered_map[s[-1]]

def main():
    solution = Solution()

    s = 'IV'

    print ('Output:', solution.romanToInt(s))


if __name__ == '__main__':
    main()