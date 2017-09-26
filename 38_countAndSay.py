class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else :
            return self.say(self.countAndSay(n-1))

    def say(self, strr):
        ind = strr[0]
        count = 0
        s = ''
        for v in strr:
            if v == ind :
                count+=1
            else:
                s += (str(count) + str(ind))
                count = 1
                ind = v
        s += (str(count) + str(v))
        return s 

def main():
    solution = Solution()

    n = 5

    print ('Output:', solution.countAndSay(n))

if __name__ == '__main__':
    main()
