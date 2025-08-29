N = int(input("Enter a number: "))
total = 0
temp = N
while temp > 0:
    digit = temp % 10
    total += digit
    temp //= 10
print("Sum of digits :", total)