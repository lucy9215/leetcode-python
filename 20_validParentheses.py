class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parentheses = {')':'(', '}':'{', ']':'['}
        stack = []
        for i in s :
            if i not in parentheses:
                stack.append(i)
            elif len(stack)!=0 and parentheses[i] == stack[-1]:
                stack.pop()
            else:
                return False 
        if len(stack) == 0:
            return True
        else :
            return False


def main():
    solution = Solution()


    # s = '{()}'
    s = '{{{{{'

    print ('Output:', solution.isValid(s))


if __name__ == '__main__':
    main()
