class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maximum = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                maximum = max(maximum, count)
                count = 0
        return max(maximum, count)


        