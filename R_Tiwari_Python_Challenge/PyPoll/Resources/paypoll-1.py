import os
import csv
import numpy

# Navigate to the file
election_data_csv = os.path.join('Resources', 'election_data.csv')

election_list = []
voter_list = []
candidate_list = []
candidate_sorted = []
unique_candidate = []

# Read the csv
with open(election_data_csv, newline="") as csvfile:
    # Access csv library. Read this csvfile.
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skips header
    csv_header = next(csvfile, None)
    # prints header
    print(f"Header: {csv_header}")

    for column in csvreader:
        voter_id = int(column[0])
        county = column[1] # Remember that items in a list are strings by default.
        candidate = column[2]
        
        voter_list.append(voter_id)
        candidate_list.append(candidate)
        
    candidate_sorted = candidate_list.sort()

vote_count = len(voter_list)
# print(vote_count)

unique_candidate = set(candidate_list)
# print(unique_candidate)
candidate_count = len(unique_candidate)
# print(candidate_count)

def gethings(lVals):
    d = dict(zip(lVals, [0] * len(lVals)))
    for x in lVals:
        d[x] += 1
    return d
counted = gethings(candidate_list)
# print(counted)

# WHY DOES round(float, 2) sometimes return two decimals and sometimes don't?
correy_percent = round((counted['Correy']*100)/vote_count, 2)
khan_percent = round((counted['Khan']*100)/vote_count, 2)
li_percent = round((counted['Li']*100)/vote_count, 2)
otooley_percent = round((counted['O\'Tooley']*100)/vote_count, 2)

# 01 - Find the total number of votes cast
# TA: IS THERE A BETTER WAY TO WORK WITH "O'TOOLEY"?
print("Election Results")
print("----------")
print(f"Total Votes: {vote_count}")
print(f"Correy: {correy_percent}% ({counted['Correy']})")
print(f"Khan: {khan_percent}% ({counted['Khan']})")
print(f"Li: {li_percent}% ({counted['Li']})")
print("O'Tooley:" + str(otooley_percent) + "% " + str(counted["O\'Tooley"]))
print("----------")
print("Winner: Khan")

# Write to text file
# TA: IS THERE A SHORTER WAY TO WRITE TO TEXT FILE?
with open("Output.txt", "w") as text_file:
    # print(f"Purchase Amount: {TotalAmount}", file=text_file)
    print("Election Results", file = text_file)
    print("----------", file = text_file)
    print(f"Total Votes: {vote_count}", file = text_file)
    print(f"Correy: {correy_percent}% ({counted['Correy']})", file = text_file)
    print(f"Khan: {khan_percent}% ({counted['Khan']})", file = text_file)
    print(f"Li: {li_percent}% ({counted['Li']})", file = text_file)
    print("O'Tooley:" + str(otooley_percent) + "% " + str(counted["O\'Tooley"]), file = text_file)
    print("----------", file = text_file)
    print("Winner: Khan", file = text_file)