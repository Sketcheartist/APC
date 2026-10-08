marks = [
    75, 82, 65, 90, 55,
    78, 88, 92, 60, 70,
    85, 76, 95, 68, 72,
    80, 58, 89, 64, 91
]

highest = marks[0]
lowest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

    if mark < lowest:
        lowest = mark

average = sum(marks) / len(marks)

above = 0
below = 0

for mark in marks:
    if mark > average:
        above += 1
    elif mark < average:
        below += 1

print("Highest marks:", highest)
print("Lowest marks:", lowest)
print("Average marks:", average)
print("Above average:", above)
print("Below average:", below)