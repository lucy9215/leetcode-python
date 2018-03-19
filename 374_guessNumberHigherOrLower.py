# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lower = 1
        upper = n
        x = (lower+upper)//2
        fb = guess(x)
        while  fb !=0:
            if fb == 1:
                lower = x +1
            elif fb ==-1:
                upper = x 
            x = (lower+upper)//2
            fb = guess(x)
        return x 

def guess(x):
    num = 10
    if x == num :
        return 0 
    elif x > num:
        return -1
    elif x < num: 
        return 1



def main():
    solution = Solution()

    print ('Output:', solution.guessNumber(10))


if __name__ == '__main__':
    main()


