class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        profit = 0 
        for i in range(1,l):
            profit+= max(0, prices[i]-prices[i-1])
        return profit



def main():
    solution = Solution()

    a = [7, 1, 5, 3, 6, 4]
    # a = [7, 6, 4, 3, 1]

    print ('Output:', solution.maxProfit(a))


if __name__ == '__main__':
    main()
