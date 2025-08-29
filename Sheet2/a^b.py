A = int(input("Enter base: "))
B = int(input("Enter exponent: "))
result = 1
i = 1
while i <= B:
    result *= A
    i += 1
print("A^B :", result)