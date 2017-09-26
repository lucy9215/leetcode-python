class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # i = 0 
        # while i<len(nums)-1:
        #     if nums[i]==nums[i+1]:
        #         nums.pop(i)
        #     else:
        #         i+=1
        # return len(nums)

        if len(nums)<=1:
            return len(nums)
        l = 0 
        for i,v in enumerate(nums[1:]):
            if nums[l]!=v:
                l+=1
                nums[l]=v
        return l+1




def main():
    solution = Solution()

    nums = [1,2,2,3,4,5,5,7,7,9,11]
    # nums = []

    print ('Output:', solution.removeDuplicates(nums))
    print(nums)


if __name__ == '__main__':
    main()