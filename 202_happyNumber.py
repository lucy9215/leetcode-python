class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = set([])
        summ = 0 
        while summ not in dic:
            while n!=0:
                summ += (n%10)**2
                n = n//10
            if summ == 1:
                return True
            elif summ in dic:
                return False
            else: 
                dic.add(summ)
                n = summ 
                summ = 0 




def main():
    solution = Solution()

    a = 7

    print ('Output:', solution.isHappy(a))


if __name__ == '__main__':
    main()
