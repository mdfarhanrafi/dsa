from typing import List


def NtimeName(name, n):
    if n == 0:
        return
    print(name)
    NtimeName(name, n-1)


def itoN(i, n):
    if i > n:
        return
    print(i)
    itoN(i+1, n)


def Ntoi(n, i):
    if n < i:
        return
    print(n)
    Ntoi(n-1, i)


def sumofN(n):
    if n == 0:
        return 0
    return n + sumofN(n-1)


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


def reverse(arr: List[int], n):
    if n == 0:
        return
    print(arr[n-1])
    reverse(arr, n-1)


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


def isPalindrome(s, i, j):
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return isPalindrome(s, i+1, j-1)
