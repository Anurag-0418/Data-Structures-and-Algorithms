class Solution:
    def daysCalc(self, weights: list[int], mid: int) -> int:
        trips = 0
        weight = 0
        for i in weights:
            if weight + i > mid:
                weight = i
                trips += 1
            else: weight += i
        if weight != 0:
            trips += 1
        return trips

    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = 0
        for i in weights:
            high += i
        while low <= high:
            mid = low + (high - low) // 2
            trips = self.daysCalc(weights, mid)
            if trips > days:
                low = mid + 1
            else:
                high = mid - 1
        return low
        