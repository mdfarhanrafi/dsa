from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        begin, end = 0, len(nums) - 1

        while begin <= end:
            mid = int((begin + end) // 2)
            if nums[mid] == target:
                return True

            if nums[begin] == nums[mid] == nums[end]:  # We can't find out which side is sorted
                begin += 1  # This drops the speed of binary search
                end -= 1

            elif nums[begin] <= nums[mid]:
                if nums[begin] <= target < nums[mid]:
                    end = mid - 1
                else:
                    begin = mid + 1
            else:
                if nums[mid] < target <= nums[end]:
                    begin = mid + 1
                else:
                    end = mid - 1
        return False


solution = Solution()
print(solution.search([2, 5, 6, 0, 0, 1, 2], 0))  # Output: True
