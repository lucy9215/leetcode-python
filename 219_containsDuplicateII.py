class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for i,v in enumerate(nums):
            if v in dic: 
                dis = (i - dic[v])
                if dis<=k:
                    return True
                else:
                    dic[v] = i 
            else:
                dic[v] = i 
        return False 



def main():
    solution = Solution()

    a = [0,1,2,0,3,4,0,5,0]

    print ('Output:', solution.containsNearbyDuplicate(a,2))


if __name__ == '__main__':
    main()