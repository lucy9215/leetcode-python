class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        r = len(s) -1
        l = 0
        while l<r:
            if not s[l].isalnum():
                l+=1
            if not s[r].isalnum():
                r-=1
            while l<r and s[l].isalnum() and s[r].isalnum():
                if s[l].lower()!=s[r].lower():
                    return False
                l+=1
                r-=1
        return True


def main():
    solution = Solution()

    a = "A man, a plan, a canal: Panama"
    a = "aa"
    # a = [7, 6, 4, 3, 1]

    print ('Output:', solution.isPalindrome(a))


if __name__ == '__main__':
    main()
