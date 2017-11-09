import re 

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = re.findall('(?i)[aiueo]',s)
        rv = re.sub('(?i)[aiueo]',lambda m: vowels.pop(), s)
        return rv
