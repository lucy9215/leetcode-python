class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 9 :
            return n 

        digit  = 1 
        count =  9 

        while n > digit*count:
            n -= digit*count
            digit+=1
            count*=10
            start = 10**(digit-1)

        num = n//digit + start
        ind = n%digit
        if ind == 0: 
            r = (num-1)%10
            return r
        else :
            r = (num//(10**(digit-ind)))%10
            return r


def main():
    solution = Solution()

    a = 10

    print ('Output:', solution.findNthDigit(a))


if __name__ == '__main__':
    main()
            # start*=10
        # start+=(n-1)/digit


