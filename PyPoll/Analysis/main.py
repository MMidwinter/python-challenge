#Import OS to enable file paths across the OS
import os

#add the CSV module
import csv

#CSV file path
election_path = os.path.join('..', 'Resources', 'election_data.csv')

VoteResults = {}
#VoteCount = {}
VoteTotal = []
CandidateVotes = []
VotePercentage = []
Winner = []
candidate_list = []
candidate_vote_tally = []

#Open the file
with open(election_path) as csvfile:

    #Specify the delimiter and read csv into dictionary
    election_reader = csv.reader(csvfile, delimiter=',')

    #print(election_reader)

    header = next(election_reader)

    for row in election_reader:
        #print(row)
        CandidateVotes.append(row[2])
        
        
    #    VoteCount = {}

    VoteTotal = len(CandidateVotes)
    #print(VoteTotal)
    
    Candidates = set(CandidateVotes)
    #print(Candidates)

    #candidate_list = Candidates
    #print(candidate_list)
    f = open("PyPoll Analysis.txt", "w")

    print("Elections Results")
    f.write("Elections Results\n")

    print("-------------------------")
    f.write("-------------------------\n")

    print("Total Votes: " + str(VoteTotal))
    f.write("Total Votes: " + str(VoteTotal) + "\n")

    print("-------------------------")
    f.write("-------------------------\n")
    
    #print the candidates and they votes and percentages
    for candidate in Candidates:

        #calculate the candidate percentage
        candidatePercentage = "{:.2%}".format(CandidateVotes.count(candidate)/VoteTotal)
        #print(candidatePercentage)
        

        print(f'{candidate}: {candidatePercentage} ({CandidateVotes.count(candidate)})')
        f.write(f'{candidate}: {candidatePercentage} ({CandidateVotes.count(candidate)})\n')
        
        candidate_list.append(candidate)
        #print(candidate_list)
        candidate_vote_tally.append(CandidateVotes.count(candidate))
        #print(candidate_vote_tally)
        
        

    
                  
    print("-------------------------")
    f.write("-------------------------\n")

    #Identify and print winner
    #My tutor David Sosa helped alot with this section, he helped me identify using the index to call the winner.
    print(f"Winnter: {candidate_list[candidate_vote_tally.index(max(candidate_vote_tally))]}")
    f.write(f"Winnter: {candidate_list[candidate_vote_tally.index(max(candidate_vote_tally))]}\n")


    print("-------------------------")
    f.write("-------------------------\n")

    f.close()

#print(Candidates)
#print(results)

