# Need to retrieve data.
# 1. The total num of votes casted
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# importing datetime module
# import datetime as dt
# # now() attribute to get present time
# now = dt.datetime.now()
# print("The time right now is ", now)

################################################################ - Direct path to file
# import csv
# # assign variable for the file 
# file_to_load = 'Resources/election_results.csv'
# # open the election results and read the file
# with open(file_to_load) as election_data:
#     print(election_data)

############################################################### - Indirect path to file
import csv
import os
# Assigns a var, loads file from the path
file_to_load = os.path.join("Resources", "election_results.csv")
# with open(file_to_load) as election_data:
#     print(election_data)

#creating a new file inside analysis folder, Assigns a var
file_to_save = os.path.join("analysis", "election_analysis.txt")
# with open(file_to_save, "w") as txt_file:
#     txt_file.write("Counties in the Election\n")
#     txt_file.write("---------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")
# Open Election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze data here
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
    #Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)





