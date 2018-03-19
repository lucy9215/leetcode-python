class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        out = list(map(str, range(1,n+1)))
        for i in range(2,n,3):
            out[i]='Fizz'
        for i in range(4,n,5):
            if out[i]=='Fizz':
                out[i]+='Buzz'
            else:
                out[i]='Buzz'
        return out 

def main():
    solution = Solution()

    a = 20

    print ('Output:', solution.fizzBuzz(a))


if __name__ == '__main__':
    main()