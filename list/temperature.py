temperatures = [
    25, 28, 30, 27, 32, 35, 31, 29, 26, 24,
    23, 30, 33, 36, 34, 28, 27, 25, 29, 31,
    32, 35, 37, 33, 30, 28, 26, 24, 27, 29
]

hottest = temperatures[0]
coldest = temperatures[0]

for temp in temperatures:
    if temp > hottest:
        hottest = temp

    if temp < coldest:
        coldest = temp

average = sum(temperatures) / len(temperatures)

above = 0
below = 0

for temp in temperatures:
    if temp > average:
        above += 1
    elif temp < average:
        below += 1

print("Hottest temperature:", hottest)
print("Coldest temperature:", coldest)
print("Average temperature:", average)
print("Days above average:", above)
print("Days below average:", below)