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

# 1. Initialize a total vore counter
total_votes = 0
# Var to store candidate names
candidate_options = []
# Dict for candidate votes
candidate_votes = {}
# Winning candidate and winning candidate Count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open Election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze data here
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1 
        # Print the candidate name from each row.
        candidate_name = row[2]
        # if candidate name does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list. 
            candidate_options.append(candidate_name)
            # Beign tracking votes
            candidate_votes[candidate_name] = 0
        # Add vote to that candidates count.
        candidate_votes[candidate_name] += 1 

with open(file_to_save, "w") as txt_file:

    election_results = (
        "Electoin Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n"
    )
    print(election_results, end="")
    # Writing to txt file
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]  
        # Calculate the % 
        vote_percentage = float( votes ) / float(total_votes) * 100 
        # print and write output after saving it to var 
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

        # Determine winning vote count and candidate
        # Determing if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winnig Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n"
    )
    txt_file.write(winning_candidate_summary)







