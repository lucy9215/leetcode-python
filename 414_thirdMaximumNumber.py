class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ndup = list(set(nums))
        ndup.sort(reverse=True)
        if len(ndup) < 3:
            return ndup[0]
        else:
            return ndup[2]


def main():
    solution = Solution()

    a = [2, 2, 3, 1]

    print ('Output:', solution.thirdMax(a))


if __name__ == '__main__':
    main()