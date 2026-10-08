numbers = [10, 21, 32, 43, 54, 65, 76, 87, 98, 19, 20, 31, 42, 53, 64]

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even numbers:", even)
print("Odd numbers:", odd)