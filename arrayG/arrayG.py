import random
import csv

# Generate a list of 64 random integers between 0 and 255
random_integers = [random.randint(0, 255) for _ in range(64)]

# Define the CSV file name
csv_file_name = 'random_integers.csv'

# Write the list to a CSV file
with open(csv_file_name, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(random_integers)

print(f"List exported to {csv_file_name}")