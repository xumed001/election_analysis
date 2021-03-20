
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

# 1: Create a county list and county votes dictionary.
county = []
county_votes = {}
largest_turnout_county = ""
largest_county_vote = 0

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
        # 3: Extract the county name from each row.
        county_name = row[1]
        # if candidate name does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list. 
            candidate_options.append(candidate_name)
            # Beign tracking votes
            candidate_votes[candidate_name] = 0
        # Add vote to that candidates count.
        candidate_votes[candidate_name] += 1 

                # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county:

            # 4b: Add the existing county to the list of counties.
            county.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] += 1

    #print(county)
    #print(county_votes)


with open(file_to_save, "w") as txt_file:

    election_results = (
        "* Electoin Results *\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n"
    )
    print(election_results, end="")
    # Writing to txt file
    txt_file.write(election_results)
    
    county_results_title = (
        f"County Votes:\n"
    )
    txt_file.write(county_results_title)

     # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Retrieve the county vote count.
        votesC = county_votes[county_name]
        # 6c: Calculate the percentage of votes for the county.
        voteC_percentage = float(votesC) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_results = (f"{county_name}: {voteC_percentage:.1f}% ({votesC:,})\n")
        #print(county_results)
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
        print(county_results)  
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votesC > largest_county_vote):
            largest_county_vote = votesC
            largest_turnout_county = county_name

     
    
    # 7: Print the county with the largest turnout to the terminal.
    largest_turnout_county_summary = (
        f"--------------------------------\n"
        f"Largest County turnout: {largest_turnout_county}\n"
        f"--------------------------------\n"
    )
    print(largest_turnout_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_turnout_county_summary)

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
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)







