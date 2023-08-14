import csv 
from pathlib import Path 
from decimal import Decimal 


def find_highest_overhead_category():
    arr = []
    highest = Decimal(0)
    highestCategory = ""
    

    print("Find highest overheads...")
    
    # Read the CSV file
    with open('csv/Overheads.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip the header

        for row in csv_reader:
            percentage = Decimal(row[1])
            
            
            if percentage > highest:
                highest = percentage
                highestCategory = row[0]

    return highestCategory, highest




