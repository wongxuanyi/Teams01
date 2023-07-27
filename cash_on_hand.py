# Import csv module, pathlib
from pathlib import Path
import csv
file_path = Path.cwd()/"COH_Sample_Data_Files"/"Cash on Hand (Deficit).csv"

# Check if file exists
print(file_path.exists())
print(file_path.is_file())

# Read csv file
with file_path.open(mode = "r", encoding= "UTF-8", newline = "") as file:
    reader = csv.reader(file)

def difference(data):
    """
    This function calculates the difference in Cash-On-Hand if the current day is lower than the previous day.
    """
    cash_difference = []
    prev_cash = data[0]["cash_on_hand"]

    for entry in data[1]:
        current_cash = entry["cash_on_hand"]
        if current_cash < prev_cash:
            cash_difference.append(current_cash - prev_cash)
        prev_cash = current_cash

    return cash_difference

def main():
    file_name = "Cash on Hand (Deficit).csv"
    file_path = Path.cwd()/"COH_Sample_Data_Files"/"Cash on Hand (Deficit).csv"

    if file_path.exists() == False: 
        return print(f"Error {file_name} does not exist.")
    
    elif file_path.is_file() == False:
        return print(f"Error {file_name} is not an actual file.")
    

    with file_path.open(mode = "r", encoding= "UTF-8", newline = "") as file:
        reader = csv.reader(file)
        data = list(reader)
    
    cash_difference_data = difference(data)

    print("Day \tCash Difference")
    print("----------------------")
    for item in cash_difference_data:
        print(f"{item['Day']} \t{item['CashDifference']:.2f}")

if __name__ == "__main__":
    main()


num = test 
