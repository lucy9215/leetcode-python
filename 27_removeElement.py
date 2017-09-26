class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        # i = 0 
        # for v in nums:
        #     if v != val:
        #         nums[i]=v
        #         i+=1
        # return i
        
        while val in nums:
            nums.pop(nums.index(val))
        return len(nums)




def main():
    solution = Solution()

    nums = [1,2,2,3,4,5,5,2,3,5,8]
    val = 2
    # nums = []

    print ('Output:', solution.removeElement(nums,val))
    print (nums)


if __name__ == '__main__':
    main()