patients = ["Rahul", "Sneha", "Amit", "Priya"]

# Add patient
patients.append("Neha")

# Search patient
name = input("Enter patient name to search: ")

if name in patients:
    print("Patient found")
else:
    print("Patient not found")

# Delete patient
name = input("Enter patient name to delete: ")

if name in patients:
    patients.remove(name)
    print("Patient deleted")
else:
    print("Patient not found")

# Display patients
print("All patients:", patients)

# Count patients
print("Total patients:", len(patients))