numbers = []

for i in range(10):
    num = int(input("Enter number: "))
    numbers.append(num)

numbers.sort()

print("Ascending:", numbers)

numbers.sort(reverse=True)

print("Descending:", numbers)