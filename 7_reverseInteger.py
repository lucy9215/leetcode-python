MAX = 2**31
MIN = -2**31 +1

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)
        if s[0]=='-':
            # print(s[-1:0:-1])
            nu = int(s[::-1][:-1])*(-1)
        else :
            nu = int(s[::-1])
        if nu > MAX or nu < MIN:
            return 0
        else:
            return nu

        

def main():
    solution = Solution()

    print(MAX,MIN)

    # x = -2544359999999
    x = -4435
    # x = 1

    print ('Output:', solution.reverse(x))


if __name__ == '__main__':
    main()