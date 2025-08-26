from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = 0
        rightmax = 0
        total = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] <= height[r]:
                if leftmax > height[l]:
                    total = total + (leftmax - height[l])
                else:
                    leftmax = height[l]
                l = l+1
            else:
                if rightmax > height[r]:
                    total = total + (rightmax - height[r])
                else:
                    rightmax = height[r]
                r = r-1

        return total
