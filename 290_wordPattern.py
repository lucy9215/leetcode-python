class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strlist = str.split()
        l = len(pattern)
        if l!=len(strlist):
            return False 
        dic = {}
        vrecord = ()
        for i in range(l):
            if pattern[i] not in dic:
                if strlist[i] not in vrecord:
                    dic[pattern[i]] = strlist[i] 
                    vrecord+=(strlist[i],)
                else:
                    return False
            if dic[pattern[i]]!= strlist[i]:
                return False
        return True



def main():
    solution = Solution()

    p = "abba"
    s = "dog cat fish dog"

    print ('Output:', solution.wordPattern(p,s))


if __name__ == '__main__':
    main()