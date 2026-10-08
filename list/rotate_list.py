numbers = [1, 2, 3, 4, 5]

# Left rotation
left = numbers[1:] + numbers[:1]

# Right rotation
right = numbers[-1:] + numbers[:-1]

print("Original:", numbers)
print("Left rotation:", left)
print("Right rotation:", right)