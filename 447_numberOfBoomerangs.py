class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        res = 0 
        for a,b in points:
            neighbors = {}
            for x,y in points:
                d = (a-x)**2 + (b-y)**2
                neighbors[d] = 1 + neighbors.get(d,0)
            for k,v in neighbors.items():
                res+=v*(v-1)
        return res 


def main():
    solution = Solution()

    a = [[0,0],[1,0],[2,0]]

    print ('Output:', solution.numberOfBoomerangs(a))


if __name__ == '__main__':
    main()