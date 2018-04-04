class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # g: greedy of child 
        # s: cookies
        lg = len(g)
        ls = len(s)
        g.sort()
        s.sort()
        summ, i, j = 0, 0, 0
        while i<lg and j<ls:
            if s[j]>=g[i]:
                summ+=1
                i+=1
                j+=1
            else:
                j+=1
        return summ 



def main():
    solution = Solution()

    g = [10,9,8,7]
    s = [5,6,7,8]

    print ('Output:', solution.findContentChildren(g,s))


if __name__ == '__main__':
    main()