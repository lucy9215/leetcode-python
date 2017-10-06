class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if a==b=='':
            return ''
        elif a=='':
            return b
        elif b=='':
            return a
            
        x = int(a,2)
        y = int(b,2)
        rstr = bin(x + y)[2:]
        return rstr


def main():
    solution = Solution()

    a = '0'
    b = '0'

    print ('Output:', solution.addBinary(a,b))


if __name__ == '__main__':
    main()