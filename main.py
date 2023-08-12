import cash_on_hand, profit_loss, overheads

def main():
    
    #calls each individual function
    profit_loss_data = profit_loss.readCSV()
    cash_on_hand_data = cash_on_hand.readCSV()
    overhead_data = overheads.readCSV()

    with open('summary_report.txt', 'w') as f:
        #loop through the data
        for y in cash_on_hand_data:
            f.write('[CASH DEFICIT] day: ')
            f.write(y[0])
            f.write(',')

            f.write('AMOUNT: USD')
            f.write(str(y[1]))
            f.write('/n')

        for x in profit_loss_data:

            f.write('[PROFIT INCREMENT] day: ')
            f.write(x[0])
            f.write(',')

            f.write('AMOUNT: USD')
            f.write(str(x[1]))
            f.write('/n')

    print('summary report done')
        

    

    