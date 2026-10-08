cities = ["Pune", "Mumbai", "Delhi", "Nashik", "Kolhapur"]

city = input("Enter city name: ")

if city in cities:
    print("City exists in the list")
else:
    print("City not found")