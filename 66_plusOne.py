class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        res = (1 + digits[-1])%9
        if res == 0 :
            digits[-1] +=1
            return digits
        else:
            l = len(digits) -1
            summ = 1 + digits[-1]
            for i in range(l):
                digits[l-i] = summ%10
                summ = summ//10
                if summ == 0 :
                    return digits
                else:
                    summ+=digits[l-i-1]
            if summ > 9:
                digits[0] = summ%10
                summ = summ//10
                digits.insert(0,summ)
            else:
                digits[0] = summ
            return digits
            

def main():
    solution = Solution()

    digits = [5,8,9,9]


    print ('Output:', solution.plusOne(digits))


if __name__ == '__main__':
    main()