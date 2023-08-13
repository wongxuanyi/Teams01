import cash_on_hand, profit_loss, overheads

def main():

    """
    this function processes cash on hand, profit and loss and overheads and generates a summery report
    """
    cash_on_hand_data= cash_on_hand.readcsv()
    Profit_loss_data = profit_loss.readcsv()
    overhead_data = overheads.find_highest_overhead_category()

    with open('summary_report.txt', 'w') as f:
        #loop through the data
        for y in cash_on_hand_data:
            f.write('[CASH DEFICIT] day: ')
            f.write(y[0])
            f.write(',')

            f.write('AMOUNT: USD')
            f.write(str(y[1]))
            f.write('\n')
        #Loops through data
        for x in Profit_loss_data:

            f.write('[NET SURPLUS] day: ')
            f.write(x[0])
            f.write(',')

            f.write('AMOUNT: USD')
            f.write(str(x[1]))
            f.write('\n')

        for z in overhead_data:
            
            f.write('[HIGHEST OVERHEADS]')
            f.write(overhead_data[0])
            f.write(': USD')
            f.write(str(overhead_data[1]))
            f.write('\n')

    print('summary report done')

main()







        

    

    
