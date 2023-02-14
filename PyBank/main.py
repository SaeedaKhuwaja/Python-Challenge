#import modules
#to handle file paths
#import os
#to handle cvs files
import csv 
import math
#store the relative file path as '../Resources/budget_data.csv
budget_data = open("Resources\Budget_data.csv", "r")
#define the variables
netchangelist = []
totalmonths = 0
netchange = []
monthofchange = []
profittotal = 0
previouschange = 0
greatestincrease = 0
greatestdecrease = 99999999999
imonth = ""
dmonth = ""

with budget_data as csvFile:
    #set up the reader for the csvfile
    csvReader = csv.reader(csvFile, delimiter = ',')
    # to skip the headers in the column use next()
    csvHeader = next(csvReader)
    # variable to hold the first row
    firstrow = next(csvReader)
    #to calculate the total number of months 
    totalmonths = totalmonths + 1
    # previousnet is the first value of the row
    previousnet = int(firstrow[1])
    
    #run a loop through the rows to find total months and profit total
    for row in csvReader:
        row.append(row[0])
        #to count the number of months
        totalmonths = totalmonths + 1
        #totalnet = totalnet + int(row[1])
        #to count the profit total
        row.append(row[1])
        #use int to convert the datatype into integer and calculate the profittotal
        profittotal = profittotal + int(row[1])
        
        # netchange is currentvalue - previousnet
        # here initial value of previousnet is the first value of the column
        netchange = int(row[1]) - previousnet
        # looping through the column to go down the column
        previousnet = int(row[1])
        #adding the values to the list 
        netchangelist = netchangelist + [netchange]
        
        #to find the averagechange divide the sum of netchangelist by the number of netchangelist
        averagechange = math.ceil(sum(netchangelist) / len(netchangelist))
        
        #Calculate the greatest increase
        #run if loop to calculate the greatestincrease
        if netchange > greatestincrease:
            greatestincrease = netchange
            imonth = row[0]

        if netchange < greatestdecrease:
            greatestdecrease = netchange
            dmonth = row[0]


    #finally print the values
    print(f"Total Months: {totalmonths}")
    print(f"Total: ${profittotal}")
    print(f"Averagechange: ${averagechange}")
    print(f"The Greatest Increase in Profits: {imonth} $({greatestincrease})")
    print(f"The Greatest Decrease in Profits: {dmonth} $({greatestdecrease})")

    #export the results to the textfile
    file = open("Analysis\mainbank.txt", 'w')
    file.write("Financial Analysis")
    file.write("\n-------------------------------")
    file.write(f"\nTotal Months: {totalmonths}")
    file.write(f"\nTotal: ${profittotal}")
    file.write(f"\nAveragechange: ${averagechange}")
    file.write(f"\nThe Greatest Increase in Profits: {imonth} $({greatestincrease})")
    file.write(f"\nThe Greatest Decrease in Profits: {dmonth} $({greatestdecrease})")
    file.close()








