class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return (n+1)*n/2 - sum(nums)




def main():
    solution = Solution()

    a = [0]

    print ('Output:', solution.missingNumber(a))


if __name__ == '__main__':
    main()