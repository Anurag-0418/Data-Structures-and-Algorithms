class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n, low = len(nums), 1
        high = n - 2
        if n == 1:
            return nums[0]
        elif nums[0] != nums[1]:
            return nums[0]
        elif nums[n - 1] != nums[n - 2]:
            return nums[n - 1]
        else:
            while(low <= high):
                mid = low + (high - low) // 2
                if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid -1]:
                    return nums[mid]
                elif mid% 2 == 0:
                    if nums[mid] == nums[mid + 1]:
                        low = mid + 1
                    else:
                        high = mid - 1
                else:
                    if nums[mid] == nums[mid + 1]:
                        high = mid - 1
                    else:
                        low = mid + 1
        return nums[low]
        