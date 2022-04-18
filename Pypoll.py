## code
#import module to read file
import csv
import os
#create variable for file and set path
#file_to_load = "Resources\election_results.csv"
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    print(election_data)


#Write down the names of all the candidates.
#Add a vote count for each candidate.
#Get the total votes for each candidate.
#Get the total votes cast for the election.
# Import the datetime class from the datetime module.


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
 

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")


# Write three counties to the file.
outfile.write("Counties in the Election\nArapahoe\nDenver\nJefferson")
# Close the file
outfile.close()