class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = nums[0]
        total = 0
        for i in nums:
            total += i
            maxi = max(total,maxi)
            if total < 0:
                total = 0
        return maxi 

        