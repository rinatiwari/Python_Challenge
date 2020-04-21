import os
import csv

udemy_csv = os.path.join("web_starter.csv")

#list to store data
title = []
price = []
subscribers = []
reviews = []
length = []
review_percent=[]

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(udemy_csv, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
# loop through
    for row in csvreader:
       #Add content of title 
        title.append(row[1])

        #Add price
        price.append(row[4])

        #Add no of subscribers
        subscribers.append(row[5])

        #Add no of reviews
        reviews.append(row[6])

        #Find course length
        length.append(row[9])

        # Determine percent of review left to 2 decimal places
        percent = round(int(row[6]) / int(row[5]), 2)
        review_percent.append(percent)

        # Get length of the course to just a number
        new_length = row[9].split(" ")
        length.append(float(new_length[0]))

#print(price)
#Zip list together
cleaned_csv = zip(title, price, subscribers, reviews, length,review_percent) 
#print(next(enumerate(cleaned_csv)))
cleaned_csv_copy=cleaned_csv
for i in cleaned_csv_copy:
        print(i)

#Set variable for output file
output_file = os.path.join("web_final.csv")

with open(output_file, "w", newline="") as datafile:
        writer = csv.writer(datafile)

#write the header row  
        writer.writerow(["Title","Price","Subscribers","Reviews","Length","Review_Percent"])
        writer.writerows(cleaned_csv)

#write in zipped rows
        writer.writerows("cleaned_csv")
