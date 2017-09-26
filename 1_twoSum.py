class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pocket = {}

        for i,v in enumerate(nums):
            res = target - v 
            if res in pocket:
                return [pocket[res],i]
            else :
                pocket[v]=i


        

def main():
    solution = Solution()

    nums = [1,8,9,3,3]
    target = 6

    print ('Output:', solution.twoSum(nums, target))


if __name__ == '__main__':
    main()