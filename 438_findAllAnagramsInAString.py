from collections import Counter

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # anagram: str with same histgram

        res = []

        lp = len(p) -1
        ls = len(s)
        pCount = Counter(p)
        mCount = Counter(s[:lp]) # from 0 to lp - 2 

        for i in range(lp, ls):
            mCount[s[i]]+=1
            if mCount == pCount:
                res.append(i-lp)
            mCount[s[i-lp]]-=1
            if mCount[s[i-lp]] == 0:
                del mCount[s[i-lp]]

        return res
