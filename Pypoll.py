import csv
import os


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Assign variable to file load and path
file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:

#Perform analysis
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)

# The data we need 
# Total number of votes cast
# Complet list of candidates who received votes
# precentage of Votes per Candidate
# Total number of Votes per Candidate
# WInner of the election

