import os
import csv

#creating the csv path
csvpath = os.path.join('Resources', 'budget_data.csv')



with open(csvpath) as csvfile:
        #variables for the future
        net_prof=0
        minp=0
        maxp=0
        change=0
        #removing the header
        csv_reader = csv.reader(csvfile, delimiter=',')
        header=next(csv_reader)
        #blank lists for data
        profit=[]
        date=[]
        #creates the profit and date lists and calculates total months
        for lines in csv_reader:
                profit.append(int(lines[1]))
                date.append(str(lines[0]))
        total=(len(profit))

        #calculates net and  average profit
        for i in range(total):
            net_prof=net_prof+profit[i]
        average_prof=net_prof/total

        #calcualtes the greatest increase and decrease using comparision
        for i in range(total-1):
            change=profit[i+1]-profit[i]
            if change>maxp:
                maxp=change
                maxd=i
            if change<minp:
                minp=change
                mind=i
        
        #gets the dates for the greatest increase and  deacrease
        min_month=date[mind]
        max_month=date[maxd]

        #prints results
        print(f"Financial Analysis:  Total Months: {total}  Total: ${net_prof}  Average Change: ${average_prof}  Greatest Increse: {max_month}-${maxp}   Greatest Decrese: {min_month}-${maxp}")

        #creates document for results
        file=open("Bank.txt","w+")
        file.write(f"Financial Analysis:  Total Months: {total}  Total: ${net_prof}  Average Change: ${average_prof}  Greatest Increse: {max_month}-${maxp}   Greatest Decrese: {min_month}-${maxp}")


