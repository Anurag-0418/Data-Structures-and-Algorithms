class Solution:
    def isGood(self, nums: List[int]) -> bool:
        arr = []
        for i in range(1, len(nums)):
            arr.append(i)
        arr.append(len(nums) - 1)
        return sorted(nums) == arr
        
        