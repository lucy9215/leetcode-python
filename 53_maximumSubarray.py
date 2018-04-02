class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Kadane's algorithm
        l = len(nums)
        if l > 0 :
            maxx = nums[0]
            dp = nums[0]
        else :
            return None
        for v in nums[1:]:
            dp = max(v, dp + v)
            print (dp)
            maxx = max(maxx, dp)
        return maxx


def main():
    solution = Solution()

    # n = [1]
    n = [-2,1,-3,4,-1,2]#,2,-5,4]

    print ('Output:', solution.maxSubArray(n))

if __name__ == '__main__':
    main()



