import csv 
from decimal import Decimal 
from pathlib import path 

def find_highest_overhead_category(file_path):
    highest = Decimal(0)
    highestCategory = ""
    

    print("Find highest overheads...")
    
    # Read the CSV file
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header

        for row in csv_reader:
            converted_amount = Decimal(row[3])
            rounded_amount = round(converted_amount, 2)
            
            if rounded_amount > highest:
                highest = rounded_amount
                highestCategory = row[1]

    return highestCategory, highest

# Example usage
file_path = path('overheads.csv')  # Replace with your file path
file_path.touch()  # Create an empty file if it doesn't exist
highest_category, highest_overhead = find_highest_overhead_category(file_path)
print("The category with the highest overhead is:", highest_category)
print("The highest overhead value is:", highest_overhead)