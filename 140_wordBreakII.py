class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
        ls = len(s)
        wb = [False]*ls

        for i in range(ls):
            if s[:i+1] in wordDict:
                if not wb[i]:
                    wb[i]=[s[:i+1], ]
                else:
                    wb[i]+=[s[:i+1], ]
            if wb[i]:
                for j in range(i+1,ls):
                    if s[i+1:j+1] in wordDict:
                        if not wb[j]:
                            wb[j]=[s[i+1:j+1], ]
                        else:
                            wb[j]+=[s[i+1:j+1], ]
        # print(wb)
        if not wb[-1]:
            return []
        else:
            mem = {ls:["",],}
            res = []
            self.pick(wb,mem,ls,ls-1, res)
            # print(mem)
            for i,v in enumerate(res):
                res[i] = res[i][1:]
            # print(res)
            return res


    def pick(self, wbl, memm, fromm, to, ress):
        # print('****',memm, fromm, to)
        if to == -1:
            ress += memm[fromm]
        if to < 0:
            return 
        words = wbl[to]
        for w in words:
            lw = len(w)
            nextt = to -lw  
            memm[to] = [' '+ w + t for t in memm[fromm]] # calcu next tail 
            self.pick(wbl, memm, to, nextt, ress)


    #  other solution 
    
        # memo = {len(s): ['']}
        # def sentences(i):
        #     if i not in memo:
        #         memo[i] = [s[i:j] + (tail and ' ' + tail)
        #                for j in range(i+1, len(s)+1)
        #                if s[i:j] in wordDict
        #                for tail in sentences(j)]
        #     return memo[i]
        # return sentences(0)





def main():
    solution = Solution()

    s = "catsanddog"
    d = ["cat", "cats", "and", "sand", "dog"]

    print ('Output:', solution.wordBreak(s,d))


if __name__ == '__main__':
    main()
    # print([a+b for a in 'abc' for b in 'def'])


