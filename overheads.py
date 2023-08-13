import csv 
from pathlib import Path 
from decimal import Decimal

def find_highest_overhead_category(file_path):
    highest = Decimal(0)
    highestCategory = ""
    

    print("Find highest overheads...")
    
    # Read the CSV file
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header

        for row in csv_reader:
            strip = row[3].replace('$','').replace(',','')
            converted_amount = Decimal(strip)
            rounded_amount = round(converted_amount,2)
            
            
            if converted_amount > highest:
                highest = rounded_amount
                highestCategory = row[1]

    return highestCategory, highest


file_path = Path('overheads.csv')  # Replace with your file path
highest_category, highest_overhead = find_highest_overhead_category(file_path)
print("The category with the highest overhead is:", highest_category)
print("The highest overhead value is:", highest_overhead)
