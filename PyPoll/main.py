from cgi import test
import os
import csv

#creates path to resource file
pypoll_csv = os.path.join("Resources", "election_data.csv")

#defining all variables
stockham_count = 0
degette_count = 0
doane_count = 0
total_count = 0
test_count = 0
sto_perc = float(0)
deg_perc = float(0)
doa_perc = float(0)

with open(pypoll_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")                         

    
    csv_header = next(csvfile)                                              #Read the header row first
   
    for row in csv_reader:                                                  #Read through each row of data after the header
        total_count = total_count + 1                                       #tallies total number of votes
        if row[1] == "Charles Casper Stockham":                                           
            stockham_count = stockham_count + 1
        elif row[1] == "Diana DeGette":                                           
            degette_count = degette_count + 1
        elif row[1] == "Raymon Anthony Doane":                                           
            doane_count = doane_count + 1
        else:                                                               #adds a vote to each candidate
            test_count = test_count + 1                                     #tests to see if string conditional works


#turns counts into percentage to match desired output
sto_perc = stockham_count/total_count*100
deg_perc = degette_count/total_count*100
doa_perc = doane_count/total_count*100

print("Election Results")
print("---------------------------------------")                        #print for interactive window
print(f"Total Votes: {total_count}")
print("---------------------------------------")
print(f'Charles Casper Stockham: {sto_perc}% ({stockham_count})')
print(f'Diana DeGette: {deg_perc}% ({degette_count})')
print(f'Raymon Anthony Doane: {doa_perc}% ({doane_count})')
print("---------------------------------------")
if stockham_count > degette_count & stockham_count > doane_count:
    print(f'Winner: Charles Casper Stockham')
elif degette_count > stockham_count & degette_count > doane_count:
    print(f'Winner: Diana DeGette')
elif doane_count > degette_count & doane_count > stockham_count:
    print(f'Winner: Raymon Anthony Doane')
elif doane_count == degette_count & doane_count == stockham_count:
    print(f'Three way tie! Battle royale!')
else:
    #doane_count == degette_count & doane_count == stockham_count & doane_count == 0:
    print(f'Nobody voted for you, even your own mother!')    
print("---------------------------------------")
#for interactive terminal viewing


#Set variable for output file
output_file = os.path.join("Analysis", "election_data_output.txt")

#Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile, delimiter=',')
    writer.writerow(["Election Results"])
    writer.writerow(["---------------------------------------"])
    writer.writerow(f'Total Votes: " {total_count}')
    writer.writerow(["---------------------------------------"])
    writer.writerow(f'Charles Casper Stockham: {sto_perc}% ({stockham_count})')
    writer.writerow(f'Diana DeGette: {deg_perc}% ({degette_count})')
    writer.writerow(f'Raymon Anthony Doane: {doa_perc}% ({doane_count})')
    writer.writerow(["---------------------------------------"])
    if stockham_count > degette_count & stockham_count > doane_count:
        writer.writerow(f'Winner: Charles Casper Stockham')
    elif degette_count > stockham_count & degette_count > doane_count:
        writer.writerow(f'Winner: Diana DeGette')
    elif doane_count > degette_count & doane_count > stockham_count:
        writer.writerow(f'Winner: Raymon Anthony Doane')
    elif doane_count == degette_count & doane_count == stockham_count:
        writer.writerow(f'Three way tie! Battle royale!')
    else:
        #doane_count == degette_count & doane_count == stockham_count & doane_count == 0:
        writer.writerow(f'Nobody voted for you, even your own mother!') 
    writer.writerow(["---------------------------------------"])
