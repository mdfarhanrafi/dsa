from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        begin, end = 0, len(nums) - 1

        while begin <= end:
            mid = int((begin + end) // 2)
            if nums[mid] == target:
                return mid

            # if the value at left is smaller than mid, from left to mid is sorted
            if nums[begin] <= nums[mid]:
                # Check if the target value is within this range
                if nums[begin] <= target < nums[mid]:
                    end = mid - 1
                else:
                    begin = mid + 1

            else:
                if nums[mid] < target <= nums[end]:
                    begin = mid + 1
                else:
                    end = mid - 1
        return -1


solution = Solution()
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))  # Output: 4
