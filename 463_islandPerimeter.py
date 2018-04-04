class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0])
        if h <1 or w < 1:
            return 0 
        res = sum(grid[0]) + sum(grid[-1])
        for row in range(1,h):
            res += sum([i^j for i,j in zip(grid[row-1],grid[row])])

        tanspose = list(map(list,zip(*grid)))
        res += sum(tanspose[0]) + sum(tanspose[-1])
        for col in range(1,w):
            res += sum([i^j for i,j in zip(tanspose[col-1],tanspose[col])])
        return res 



def main():
    solution = Solution()

    a = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
    # print(a)
    # print(list(map(list, zip(*a))))

    print ('Output:', solution.islandPerimeter(a))


if __name__ == '__main__':
    main()