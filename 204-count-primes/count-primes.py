class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        number = [1] * (n)
        for i in range(2, n):
            if number[i] == 1:
                count += 1
                for j in range(i*i, n, i):
                    number[j] = 0
        return count




