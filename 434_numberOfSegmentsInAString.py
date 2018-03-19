class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # count = 0 
        # for i,v in enumerate(s):
        #     if v!=' ' and (i==0 or s[i-1]==' '):
        #         count+=1

        count = len([i for i in s.split(' ') if i!=''])
        return count


def main():
    solution = Solution()

    a = "Hello, my name is John"
    # a = ""
    a = "      "

    print ('Output:', solution.countSegments(a))


if __name__ == '__main__':
    main()