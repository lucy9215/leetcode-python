class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0 
        isPrime = [True]*(n)
        isPrime[0]=False
        isPrime[1]=False
        for i in range(int(n**0.5)+1):
            if isPrime[i]:
                isPrime[i*i:n:i] = [False]*len(isPrime[i*i:n:i])
        return sum(isPrime)

