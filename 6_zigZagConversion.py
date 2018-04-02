class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 :
            return s 
        inc = 1 
        buff = ['']*numRows
        lenn = len(s)
        ind = 0 
        i = 0 
        while i<lenn:
            buff[ind] += s[i]
            ind +=inc
            if ind==numRows:
                ind = numRows-2
                inc = -1
            if ind==-1:
                ind = 1
                inc = 1 
            i+=1
        res = ''.join(buff)
        return res





def main():
    solution = Solution()

    a = 'PAYPALISHIRING'
    numRows = 3

    print ('Output:', solution.convert(a, numRows))


if __name__ == '__main__':
    main()