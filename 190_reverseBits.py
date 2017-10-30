class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = bin(n)[2:]
        s = s.zfill(32)[::-1]
        num = int(s,2)
        return num

def main():
    solution = Solution()

    a = 0

    print ('Output:', solution.reverseBits(a))


if __name__ == '__main__':
    main()