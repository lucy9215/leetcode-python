class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1

        low, high = 0, len(nums)-1

        while low <= high:
            mid = (high+low)//2

            if nums[mid]==target:
                return mid

            if nums[mid] >= nums[low]:
                if nums[low]<=target<=nums[mid]:
                    high = mid -1 
                else:
                    low = mid +1 
            else:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid -1 

        return -1 



def main():
    solution = Solution()

    # a = [4,5,6,7,0,1,2]
    a = [3,1]

    print ('Output:', solution.search(a,2))


if __name__ == '__main__':
    main()

