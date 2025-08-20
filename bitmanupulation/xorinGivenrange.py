
def Xor(number: int) -> int:
    if number % 4 == 0:
        return number
    elif number % 4 == 1:
        return 1
    elif number % 4 == 2:
        return number + 1
    else:
        return 0


l = int(input())
r = int(input())

result = Xor(r) ^ Xor(l - 1)

print(result)
