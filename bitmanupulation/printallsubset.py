def generate_subsets(arr):
    n = len(arr)
    subsets = []

    for mask in range(1 << n):  # loop through 0 to 2^n - 1
        subset = []
        for i in range(n):
            if mask & (1 << i):  # check if i-th bit is set
                subset.append(arr[i])
        subsets.append(subset)

    return subsets


# Example usage
arr = [1, 2, 3]
for subset in generate_subsets(arr):
    print(subset)
