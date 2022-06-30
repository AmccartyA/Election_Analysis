import csv
import os


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Assign variable to file load and path
file_to_load = os.path.join("Resources", "election_results.csv")

#Initialize vote counter
total_votes = 0

#options and votes
candidate_options = []

#empty Dicts
candidate_votes = {}

#Winning Candidate Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Perform analysis
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)

    for row in file_reader:

        total_votes +=1

        #get candidate name
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            candidate_votes[candidate_name] = 0
            
        candidate_votes[candidate_name] += 1
#Save results to text file
with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection\n"
        f"------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------\n")
    print (election_results, end="")

    txt_file.write(election_results)
    
        #Dertermine percentage of votes
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes)*100
        candidate_results = (
            f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print (candidate_results)
        txt_file.write(candidate_results)
        
    #Determine Winning Votes
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name       
    winning_candidate_summary = (
        f'------------------------\n'
        f'Winner:{winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage:{winning_percentage:.1f}&\n'
        f'--------------------------\n')
    print (winning_candidate_summary)

    txt_file.write(winning_candidate_summary)