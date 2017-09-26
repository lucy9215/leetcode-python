class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x >= 0 :
            return x == int(str(x)[::-1])
        else :
            return False 



def main():
    solution = Solution()


    # x = -2544359999999
    # x = -4435
    x = 123454321

    print ('Output:', solution.isPalindrome(x))


if __name__ == '__main__':
    main()
                