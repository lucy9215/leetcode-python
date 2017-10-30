class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pocket = {}
        thresh = len(nums)/2.0
        if thresh<=1:
            return nums[0]
        for v in nums:
            if v in pocket:
                pocket[v]+=1
                if pocket[v]>thresh:
                    return v 
            else :
                pocket[v]=1
            

def main():
    solution = Solution()

    a = [5,6,6]

    print ('Output:', solution.majorityElement(a))


if __name__ == '__main__':
    main()