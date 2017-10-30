class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        l = len(s)
        dic = {} # no repeating key
        note = set([]) # no repeating value
        for i in range(l):
            if s[i] in dic:
                if dic[s[i]]!=t[i]:
                    return False
            elif t[i] not in note: 
                note.add(t[i]) 
                dic[s[i]] = t[i]
            else: 
                return False
        return True