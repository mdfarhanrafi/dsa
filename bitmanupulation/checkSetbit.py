num = int(input("Enter number: "))
i = int(input("Enter bit position: "))

print("True" if num & (1 << i) else "False")
