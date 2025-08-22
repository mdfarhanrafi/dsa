from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while (low <= high):
            count = 1
            curr_sum = 0
            mid = (low+high) // 2
            for num in nums:
                if curr_sum + num > mid:
                    count += 1
                    curr_sum = 0
                curr_sum += num

            if count <= k:
                high = mid - 1
            else:   # not feasible, need larger sum
                low = mid + 1
        return low
