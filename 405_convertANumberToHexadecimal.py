class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # if num < 0:
        #     r = self.toHex(2**32+num|0x80000000)
        # elif num==0:
        #     return '0'
        # else:
        #     return hex(num)
        # return r 

        if num < 0:
            r = self.toHex(2**32+num|0x80000000)
        elif num==0:
            return '0'
        else:
            r = ''
            while num!=0:
                digit = num%16
                if digit<10:
                    d = chr(digit+ord('0'))
                else:
                    d = chr(digit-10+ord('a'))
                r = d + r 
                num = num>>4 
        return r 


def main():
    solution = Solution()

    a = -1

    print ('Output:', solution.toHex(a))


if __name__ == '__main__':
    main()