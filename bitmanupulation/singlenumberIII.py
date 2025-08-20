# there would be array where every element occure twice except two element ## which occur once

n = int(input())

arr = list(map(int, input().split()))
xorr = 0
for i in range(n):
    xorr = arr[i] ^ xorr

rightmost = (xorr & xorr - 1) & xorr
first = 0
second = 0

for i in range(n):
    if arr[i] & rightmost:
        print(arr[i] & rightmost)
        first = first ^ arr[i]
    else:
        second = second ^ arr[i]

print("First unique number:", first)
print("Second unique number:", second)


# print(4 ^ 0)
