class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s = set([])
        # for v in nums:
        #     if v in s:
        #         s.remove(v)
        #     else:
        #         s.add(v)
        # return s.pop()

        # more efficient using XOR
        ini = 0 
        for v in nums:
            ini ^=v
        return ini


def main():
    solution = Solution()

    a = [2,2,1]

    print ('Output:', solution.singleNumber(a))


if __name__ == '__main__':
    main()