# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1 
        ts = isBadVersion(s)
        if ts:
            return s 
        e = n 
        te = isBadVersion(e)
        if not te:
            return e 
        while e-s>1:
            i = (e+s)//2
            ti = isBadVersion(i)
            if ti!=ts:
                e = i 
                te = ti
            else:
                s = i 
                ts = ti 
        return e 
        # class Wrap:
        #     def __getitem__(self, i):
        #         return isBadVersion(i)
        # return bisect.bisect(Wrap(), False,1,n) # from index 1 to index n 