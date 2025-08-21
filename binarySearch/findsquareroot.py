

def squareroot(n):
    low = 0
    high = n
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid

        if square == n:
            return mid
        elif square < n:
            ans = mid  # Potential answer
            low = mid + 1
        else:
            high = mid - 1

    return ans


# Example usage
n = 16
ans = squareroot(n)
print("The square root of", n, "is approximately:", ans)
