#Import OS to enable file paths across the OS
import os

#add the CSV module
import csv

#CSV file path
election_path = os.path.join('..', 'Resources', 'election_data.csv')

VoteTotal = []
CandidateVotes = []
VotePercentage = []
Winner = []

#Open the file
with open(election_path) as csvfile:

    #Specify the delimiter and read csv into dictionary
    election_reader = csv.reader(csvfile, delimiter=',')

    #print(election_reader)

    header = next(election_reader)

    for row in election_reader:
        #print(row)
        CandidateVotes.append(row[2])

    VoteTotal = len(CandidateVotes)
    #print(VoteTotal)
    
    Candidates = set(CandidateVotes)
    #print(Candidates)

candidate_list = Candidates
print(candidate_list)

results = dict()

results = {"name" : candidate_list}
print(CandidateVotes.count("Khan"))
print("Elections Results")
print("-------------------------")
print("Total Votes: " + str(VoteTotal))
print("-------------------------")
print("Khan: " + "Placeholder" + " (" + CandidateVotes.count("Khan") + ")")
print("Correy: " + "Placeholder" + " (" + "Placeholder" + ")")
print("Li: " + "Placeholder" + " (" + "Placeholder" + ")")
print("O'Tooley: " + "Placeholder" + " (" + "Placeholder" + ")")
#print(Candidates)
#print(results)

