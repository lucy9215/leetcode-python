class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf'),]
        i, maxd = 0, 0 
        houses.sort()
        for x in houses:
            while x >= (heaters[i]+heaters[i+1])/2.0:
                i += 1
            maxd = max(maxd, abs(heaters[i] - x))
        return maxd

def main():
    solution = Solution()

    houses, heaters = [1,2,3,4],[1,4]

    print ('Output:', solution.findRadius(houses, heaters))


if __name__ == '__main__':
    main()




            