numbers = [1, 2, 2, 3, 1, 4, 3, 5]

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Original list:", numbers)
print("After removing duplicates:", unique)