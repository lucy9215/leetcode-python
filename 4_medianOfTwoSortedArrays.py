class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        while i < m and j <n :
            if nums1[i] > nums2[j]:
                minn = nums2[j]
                j+=1
            else:
                minn = nums1[i]
                i+=1
            nums.append(minn)
        if i < m :
            nums+=nums1[i:]
        if j < n :
            nums+=nums2[j:]
        l = len(nums)
        # print ('length:',l,', nums',nums)
        if l%2 == 0:
            i = int(l/2)
            return (nums[i -1 ] + nums[i])/2
        else:
            i = int(l/2)
            return nums[i]

def main():

    solution = Solution()

    # nums1 = [1,3]
    # nums2 = [2,]
    nums1 = [1,3]
    nums2 = [2]

    print ('Output:', solution.findMedianSortedArrays(nums1, nums2))


if __name__ == '__main__':
    main()