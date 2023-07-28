from pathlib import path 
import csv
import glob

def readcsv ():
    arr = []

    curr_day = 0 
    curr_amt = 0

    prev_day = 0
    prev_amt = 0

#Open CSV file 
with open(____) as csv_file:
    csv_reader = csv.read(csv.file, delimiter = ',')
    linecount = 0

#Loop through content 
    for row in csv_reader:
#If there is only one line in file, use that line
        if linecount == 1:
            curr_day = row[0]
            curr_amt = row [4]

#if there is more than one line 
#Checking for difference 
        if linecount > 1: 
            prev_day = curr_day
            prev_amt = curr_amt

            curr_day = row[0]

        if curr_amt < prev_amt:
            difference = prev_amt - curr_amt

        if curr_amt > prev_amt :
            highest_profit = curr_amt

          test_example  
        

   
    
