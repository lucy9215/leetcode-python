class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        include = 0 
        exclude = 0 
        for v in nums:
            tmp = include 
            include = v + exclude
            exclude = max(tmp, exclude)
        return max(include, exclude)