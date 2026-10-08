salaries = [25000, 35000, 45000, 55000, 60000, 28000, 75000]

highest = salaries[0]
lowest = salaries[0]

for salary in salaries:
    if salary > highest:
        highest = salary

    if salary < lowest:
        lowest = salary

average = sum(salaries) / len(salaries)

above_50000 = 0
below_30000 = 0

for salary in salaries:
    if salary > 50000:
        above_50000 += 1

    if salary < 30000:
        below_30000 += 1

print("Highest salary:", highest)
print("Lowest salary:", lowest)
print("Average salary:", average)
print("Employees above 50000:", above_50000)
print("Employees below 30000:", below_30000)