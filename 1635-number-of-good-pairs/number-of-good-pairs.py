class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        numbers = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    numbers += 1
        return numbers

        