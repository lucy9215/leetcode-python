class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        l_set = len(set(nums))
        dup = l>l_set
        return dup



def main():
    solution = Solution()

    a = [1,1]

    print ('Output:', solution.containsDuplicate(a))


if __name__ == '__main__':
    main()