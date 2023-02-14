#import modules
#to handle cvs files
import csv 
#store the relative file path as '..\Resources\budget_data.csv and open the file
election_data = open("Resources\election_data.csv", "r")
#set the variables
total_votes = 0
candidates = []
vote_count = {}
charles_votecount = 0
diana_votecount = 0
raymon_votecount = 0
winner = 0

with election_data as csvFile:
    #set up the reader for the csvfile
    csvReader = csv.reader(csvFile, delimiter = ',')
    # to skip the headers in the column use next()
    csvHeader = next(csvReader)
    #run loop through the file to calculate total number of votes
    for row in csvReader:
        #going down the row to calculate total votes
        total_votes = total_votes + 1

        # run if loop to make a list of candidates by creating an empty list "candidate" and an empty dictionary "vote_count"
        if (row[2]) not in candidates:
            candidates.append(row[2])
            vote_count[row[2]] = 1
        else:
            #if the name of candidate is in the list keep adding one to the votecount
            vote_count[row[2]] += 1

#print the results
print(f"Total Votes = {total_votes}")

#run a loop through the dictionary to find candidates vote percentage
for x in vote_count:
    Candidatepercent = round(vote_count[x]/ total_votes * 100, 3)
    # this wil print candidates name with their percentages
    print(f"{x} : {Candidatepercent}% ({vote_count[x]})")

    #to find the candidates with highest number of votes
    #run a if loop
    if Candidatepercent > winner:
        winner = Candidatepercent
        winner_name = x

#print the winner name
print(f"Winner: {winner_name}")

#export the results to the text file use file.write
file = open("Analysis\mainpoll.txt", 'w')
file.write("Election Results")
file.write("\n---------------------")
file.write(f"\nTotal Votes = {total_votes}")
file.write("\n---------------------")
for x in vote_count:
    Candidatepercent = round(vote_count[x]/ total_votes * 100, 3)
    
    file.write(f"\n{x} : {Candidatepercent}% ({vote_count[x]})")

    if Candidatepercent > winner:
        winner = Candidatepercent
        winner_name = x
file.write("\n---------------------")
file.write(f"\nWinner: {winner_name}")
file.write("\n---------------------")
file.close()