from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recurPermute(index: int):
            if index == len(nums):
                ans.append(nums[:])  # make a copy
                return
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]  # swap
                recurPermute(index + 1)
                # backtrack (undo swap)
                nums[index], nums[i] = nums[i], nums[index]

        recurPermute(0)
        return ans


if __name__ == "__main__":
    nums = [1, 2, 3]
    obj = Solution()
    ans = obj.permute(nums)
    print("All permutations are:")
    for perm in ans:
        print(perm)
