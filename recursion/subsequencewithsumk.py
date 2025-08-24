

def findSubsequences(curr, arr, subArr, res, k):

    # Base case: When we reach the end of the array,
    # add the current subsequence to the result
    if curr == len(arr):
        if sum(subArr) == k:
            res.append(subArr.copy())
        return

    #  Include the current element in the subsequence
    subArr.append(arr[curr])

    # Recurse to the next element
    findSubsequences(curr + 1, arr, subArr, res, k)

    # Backtrack: Remove the current element and
    # explore the next possibility
    subArr.pop()

    #  Do not include the current element in the subsequence
    findSubsequences(curr + 1, arr, subArr, res, k)


if __name__ == "__main__":
    arr = [10, 1, 2, 7, 6, 1, 5]

    k = 8
    # Temporary list to store the
    # current subsequence
    subArr = []

    # Resultant list to store all subsequences
    res = []

    sorted(arr)

    # Call the function to find all subsequences
    # starting from index 0
    findSubsequences(0, arr, subArr, res, k)

    for subsequence in res:
        print(" ".join(map(str, subsequence)))


# just only once check sum of subarray is equal to k or not


# def findSubsequences(curr, arr, subArr, res, k):

#     # Base case: When we reach the end of the array,
#     # add the current subsequence to the result
#     if curr == len(arr):
#         if sum(subArr) == k:
#             res.append(subArr.copy())
#             return True
#         return False

#     #  Include the current element in the subsequence
#     subArr.append(arr[curr])

#     # Recurse to the next element
#     if findSubsequences(curr + 1, arr, subArr, res, k):
#         return True

#     # Backtrack: Remove the current element and
#     # explore the next possibility
#     subArr.pop()

#     #  Do not include the current element in the subsequence
#     if findSubsequences(curr + 1, arr, subArr, res, k):
#         return True

#     return False


# if __name__ == "__main__":
#     arr = [1, 2, 3]

#     k = 3
#     # Temporary list to store the
#     # current subsequence
#     subArr = []

#     # Resultant list to store all subsequences
#     res = []

#     # Call the function to find all subsequences
#     # starting from index 0
#     findSubsequences(0, arr, subArr, res, k)

#     for subsequence in res:
#         print(" ".join(map(str, subsequence)))
