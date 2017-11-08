class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False 
        
        offset = ord('a') 
        hist = [0]*26

        for v in s:
            hist[ord(v)-offset]+=1
        for v in t:
            hist[ord(v)-offset]-=1

        if hist==[0]*26:
            return True
        else:
            return False


