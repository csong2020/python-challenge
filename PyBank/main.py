import os
import csv

pybank_csv = os.path.join("Resources", "budget_data.csv")

date_great = []
date_least = []                                                              #list for temporarily storing month and day
great_date_day = str
great_date_month = str
least_date_day = str
least_date_month = str
increase_rev = float(0)
decrease_rev = float(0)
revenue = float(0)
great_rev = 0
least_rev = 0
rowcount = float(0)

with open(pybank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")                         #separates day from month

    
    csv_header = next(csvfile)                                              #Read the header row first
    print("Financial Analysis")
    print("---------------------------------------")                        #For interactive terminal viewing

    for row in csv_reader:                                                  #Read through each row of data after the header
        rowcount = rowcount + 1
        if float(row[1]) > 0:                                               #Convert row to int and compare to greatest revenue number
            
            increase_rev = increase_rev + float(row[1])
            
            if float(row[1]) > great_rev:
                great_rev = float(row[1])                                   #changese greatest revenue increase value to current value if more positive
                date_great.append(row[0])                                   #adds date to the end of the list

                #https://stackoverflow.com/questions/6696027/how-to-split-elements-of-a-list (modified to fit this code)
                #[great_date_day.split('-', 1)[-1] for great_date_day in date_great]                     #separates date delimiting using "-", takes last entry

                #great_date_day = date_temp[1]                               #stores greatest increase day
                #great_date_month = date_great[-1]                             #stores greatest increase month
                #date_temp.clear                                         #clears date_temp
                

        #increase_rev = increase_rev + float(row[1])                     #adds to the positive revenue tracker


        if float(row[1]) < 0:                                               #Convert row to int and compare to greatest revenue number
            
            decrease_rev = decrease_rev + float(row[1])
            
            if float(row[1]) < least_rev:
                least_rev = float(row[1])                                   #changese greatest revenue decrease value to current value if more negative
                date_least.append(row[0])                                    #adds date to the list

                #https://stackoverflow.com/questions/6696027/how-to-split-elements-of-a-list (modified to fit this code)
                #least_date_day_test = [least_date_day.split('-', 1)[-1] for least_date_day in date_least]                     #separates date delimiting using "-", takes last entry

                #least_date_day = date_least[-1]                               #stores greatest decrease day
                #least_date_month = date_least[-1]                             #stores greatest decrease month
                #date_temp.clear                                             #clears date_temp
                

                #[i.split('-', 1)[0] for i in date_l]                                     


            #decrease_rev = decrease_rev + float(row[1])                     #adds to the negative revenue tracker
    
    date_g = date_great.pop()                                             #takes last entry in list and assigns it to date_g. It should be the date with the greatest increase
    date_l = date_least.pop()                                             #takes last entry in list and assigns it to date_l. It should be the date with the greatest decrease
    revenue = increase_rev + decrease_rev                                   #calculates total revenue
    avg_change = int(revenue/rowcount)                                      #calculates average change
    
    print(f"Total Months: {int(rowcount)}")
    print(f"Total: ${float(revenue)}")
    print(f"Average Change: ${float(avg_change)}")
    print(f"Greatest Incrase in Profit: {date_g} (${float(great_rev)})")
    print(f"Greatest Decrease in Profit: {date_l} (${float(least_rev)})")   #for interactive terminal viewing


#zips variables together to print to output file
#cleaned_csv = zip(rowcount, revenue, avg_change, great_date_month, great_date_day, great_rev, least_date_month, least_date_day, least_rev)

#Set variable for output file
#output_file = os.path.join("budget_data.csv")
output_file = os.path.join("Analysis", "budget_data_output.txt")

#Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Financial Analysis"])
    writer.writerow(["---------------------------------------"])
    writer.writerow(["Total Months: ", rowcount])
    writer.writerow(["Total: $", revenue])
    writer.writerow(["Average Change: $", avg_change])
    writer.writerow(f'Greatest Increase in Profits: , {date_g} ({great_rev})')
    writer.writerow(f'Greatest Decrease in Profits: , {date_l} ({least_rev})')

    #Write in zipped rows
    #writer.writerows(cleaned_csv)