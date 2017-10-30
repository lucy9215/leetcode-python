class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        tmp = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k]=tmp


def main():
    solution = Solution()

    a = [1,2,3]

    print ('Output:', solution.rotate(a,2),a)


if __name__ == '__main__':
    main()