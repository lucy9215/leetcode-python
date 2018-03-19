class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        base = ord('0')
        n1 = 0  
        n2 = 0 
        for v in num1:
            n1=n1*10+(ord(v)-base)
        for v in num2:
            n2=n2*10+(ord(v)-base)
        summ = str(n1+n2)
        return summ 

def main():
    solution = Solution()

    a = '0'
    b = '99'

    print ('Output:', solution.addStrings(a,b))


if __name__ == '__main__':
    main()