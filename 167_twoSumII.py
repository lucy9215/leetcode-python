class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pocket = {}
        for i,v in enumerate(numbers):
            res = target - v 
            if res in pocket:
                return [pocket[res],i+1]
            else :
                pocket[v] = i+1
