class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num//10!=0:
            num = sum([int(digit) for digit in str(num)])
        return num

