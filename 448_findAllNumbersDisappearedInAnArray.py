class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        snums = set(nums)
        n = len(nums)
        onums = set([i for i in range(1,n+1)])
        res = list(onums - snums)
        return res 