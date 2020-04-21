import os
import csv

#making dictionary of the file
def keywithmaxval(d):
	     """ a) create a list of the dict's keys and values; 
	         b) return the key with the max value"""  
	     v=list(d.values())
	     k=list(d.keys())
	     return k[v.index(max(v))]
	
#locate the csv file 
election_data_csv = os.path.join("Resources","election_data.csv")
#read csv file
with open(election_data_csv, newline="") as csvfile:
	        csvreader = csv.reader(csvfile, delimiter=',')
	        next(csvreader)
	

	        totalVotes=0
	        candidates=[]
	

	        votes_per_candidate = {}
	        for row in csvreader:
	            totalVotes=totalVotes+1
	            if row[2] not in candidates:
	                candidates.append(row[2])
	                votes_per_candidate.update({row[2]:1})
	            else:
	                votes_per_candidate.update({row[2]:votes_per_candidate[row[2]]+1})
	

# Add the dict values if the candidate is in the list and find the percentages with 3f

	        candidate_percentages={}
	        for key,value in votes_per_candidate.items():
	            candidate_percentages.update({key:str(round(100*value/totalVotes,3))+"%"})
	    
	    
	        Winner=keywithmaxval(votes_per_candidate)
	

	        print()
	        print()
	        print("Election Results")
	        print("-------------------------")
	        print(f"Total Votes: {totalVotes}")
	        print("-------------------------")        
	        for candidate in candidates:
	            print(f"{candidate}: {candidate_percentages[candidate]} ({votes_per_candidate[candidate]})")
	        print("-------------------------")  
	        print(f"Winner: {Winner}")
	        print("-------------------------")  
	        print()
