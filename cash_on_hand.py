from pathlib import Path 
import csv

#Create a function that reads the date in CSV file
def readcsv ():

    curr_day = 0 
    curr_amt = 0

    prev_day = 0
    prev_amt = 0

#Open CSV file 
    with open('Profit & Loss (Surplus).csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        linecount = 0
        highest_profit = 0
#Loop through content 
        for row in csv_reader:
#If there is only one line in file, use that line
            
            if linecount == 1:
                curr_day = row[0]
                curr_amt = row [4]

#if there is more than one line 
 
            if linecount > 1:
                prev_amt = curr_amt

                curr_amt = row[4]
#Checking for difference
                if curr_amt < prev_amt:
                    difference = prev_amt - curr_amt
#Checking if amount is increasing, then take the highest
                if curr_amt >= prev_amt :
                    highest_profit = curr_amt
#Go through all the line                     
            linecount = linecount + 1
        print(highest_profit)        
        
readcsv()