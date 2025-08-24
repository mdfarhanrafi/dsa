def bin_exp(base: int, pow: int) -> int:
    # base case
    if pow == 0:
        return 1

    # recursive step
    half = bin_exp(base, pow // 2)

    if pow % 2 == 0:
        return half * half
    else:
        return half * half * base


if __name__ == "__main__":
    a, b = 2, 10
    print(f"{a}^{b} =", bin_exp(a, b))  # 1024
