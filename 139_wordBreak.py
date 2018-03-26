class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        ls = len(s)

        wb = [False]*ls

        for i in range(ls):
            if (wb[i]==False) and (s[:i+1] in wordDict):
                wb[i]=True
                if i+1==ls:
                    return True
            if wb[i]:
                for j in range(i+1,ls):
                    if (wb[j]==False) and (s[i+1:j+1] in wordDict):
                        wb[j]=True
                        if j+1==ls:
                            return True
        # print(wb)
        res = wb[-1]
        return res

        # below is stylish code which is the same principle 
        
        # ok = [True]
        # for i in range(1, len(s)+1):
        #     ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        # return ok[-1]



def main():
    solution = Solution()

    s = "leetcode"
    d = ["leet", "code"]

    print ('Output:', solution.wordBreak(s,d))


if __name__ == '__main__':
    main()

