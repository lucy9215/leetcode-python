class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero = 0 
        for i in range(n):
            if nums[i]:
                if i!=zero:
                    nums[i],nums[zero] = nums[zero],nums[i]
                zero+=1


def main():
    solution = Solution()

    a = [1,0,3,12]
    # a = [0]

    print ('Output:', solution.moveZeroes(a),a)


if __name__ == '__main__':
    main()