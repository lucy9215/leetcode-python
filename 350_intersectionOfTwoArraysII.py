from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 = len(nums2)
        if l1<l2:
            nums1,nums2 = nums2,nums1
        c1 = Counter(nums1)
        intersec = []
        for v in nums2:
            if v in c1 and c1[v]>0:
                ci[v]-=1
                intersec.append(v)
        return intersec


        # c1 = Counter(nums1)
        # c2 = Counter(nums2)
        # intersec = [[num]*min(c1[num],c2[num]) for num in c1&c2] 
        # return intersec

        