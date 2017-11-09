class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        accunum = [0,]
        summ = 0 
        for v in nums:
            summ+=v
            accunum.append(summ)
        self.accunum = accunum

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i <= j:
            summ = self.accunum[j+1]-self.accunum[i]
            return summ
        else:
            return 
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)