class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # ss = s+s[1:-1] contains all rotated version of s.
        # 将s分作等长sub string, ss 中一定有其循环移位的string，如果与移位的str相等，那么说明s的这种划分是周期的
        if not s:
            return

        return s in (s+s)[1:-1]