class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 0
        i = 1
        while i * i <= num:
            if num % i == 0:
                sum += i
                if num // i != i:
                    sum += num // i
            i += 1
        return sum == num * 2
        