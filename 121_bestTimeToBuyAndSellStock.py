class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # form prices_diff start from prices[1] by (prices[i]-prices[i-1]), 
        # then this question became a max subsequence problem, which could solved by 
        # Kadane's Algorithm
        maxcur = 0 
        maxsofar = 0 
        l = len(prices)
        for  i in range(1,l):
            maxcur = max(0, maxcur+ prices[i]-prices[i-1])
            maxsofar = max(maxcur,maxsofar)
        return maxsofar


def main():
    solution = Solution()

    a = [7, 1, 5, 3, 6, 4]
    # a = [7, 6, 4, 3, 1]

    print ('Output:', solution.maxProfit(a))


if __name__ == '__main__':
    main()
