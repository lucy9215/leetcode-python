class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        if not nums:
            return False

        low, high = 0, len(nums)-1

        while low <= high:
            mid = (high+low)//2

            if nums[mid]==target:
                return True

            if nums[mid] > nums[low]:
                if nums[low]<=target<=nums[mid]:
                    high = mid -1 
                else:
                    low = mid +1 
            elif nums[mid] < nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low = mid+1
                else:
                    high = mid -1 
            else:
                if nums[mid]==nums[low]:
                    low += 1
                if nums[mid]==nums[high]:
                    high -= 1 
        return False



def main():
    solution = Solution()

    # a = [4,5,6,7,0,1,2]
    a = [1,1,1,3,1,1,1]

    print ('Output:', solution.search(a,3))


if __name__ == '__main__':
    main()

