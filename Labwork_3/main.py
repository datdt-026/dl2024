import csv
import random

# Generate 30 random data entries
data = []
for _ in range(50):
    salary = random.randint(1, 50)  # Generate random salary between 1 and 50 million VND
    experience = random.randint(1, 15)  # Generate random experience between 1 and 15 years
    loan = random.choice([0, 1])  # Randomly choose 0 or 1 for loan status
    data.append({"Salary (M VND)": salary, "Experience (year)": experience, "Loan (1 or 0)": loan})

# Specify the file name
filename = "employee_data.csv"

# Writing to CSV file
with open(filename, 'w', newline='') as csvfile:
    # Define fieldnames
    fieldnames = ["Salary (M VND)", "Experience (year)", "Loan (1 or 0)"]

    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    writer.writerows(data)

print(f"CSV file '{filename}' created successfully with 30 items.")
