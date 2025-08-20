from typing import List


def unique(nums: List[int]) -> int:
    unique_num = 0
    for num in nums:
        unique_num ^= num   # XOR cancels duplicates
    return unique_num


n = int(input("Enter number of elements: "))
nums = list(map(int, input().split()))  # take all numbers in one line

print(unique(nums))
