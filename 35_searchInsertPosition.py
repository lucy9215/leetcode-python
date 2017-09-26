class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)>0 and target > nums[-1]:
            return len(nums)
        for i,v in enumerate(nums):
            if v >= target:
                return i 
        return 0 


def main():
    solution = Solution()

    # nums = [1,3,6,8,9]
    nums = []
    target = 6

    print ('Output:', solution.searchInsert(nums, target))


if __name__ == '__main__':
    main()