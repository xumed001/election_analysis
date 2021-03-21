# Election_Analysis
## Project Overview
Extracting Data from an election audit of a local congressional election.

1. Calculates the total number of votes casted and the list of candidates.
2. Calculates the total number of votes each candidate received and the percentage of votes they won.
3. Determine the election winner based on popular vote.
4. Calculates County with the largest number of voters.
5. Calculates each County and its total vote and the percentage of votes they casted. 

## Resources
- Data source: election_results.csv
- Software used: Visual Studio Code 1.54.3, Python 3.8.5

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:<br/>
     - Charles Casper Stockham.
     - Diana DeGette. 
     - Raymon Anthony Doane. 
- Their vote distribution:<br/>
     - Charles Casper Stockham received 23.0% of the vote with the vote count of 85,213.
     - Diana DeGette received  73.8% of the vote with the vote count of 272,892. 
     - Raymon Anthony Doane received  3.1% of the total vote with the vote count of 11,606. 
- The winner of the election was: <br/>
     - Diana DeGette receiving 73.8% of the total vote with the vote count of 272,892.
- The analysis of the election filtered by county show that:
     - Denver County had the largest number of voter turnout.<br/>
    
## Challange Overview
Adding additional info and filtering the data by County to better understand the election audit of a local congressional election.

## Challange Summary
The purpose of this proposal is to introduce a short script that will better aid with the election process. It is a Python script that will process large election data and print out the election results in a easy to digest text file. The script requires election data in a .csv file format. To use the script some modifications will be needed:
- First, change the source (file_to_load) to add your source file and export (file_to_save) to any destination you want.
- Second, if needed change line 47 (candidates name) & 49 (county name)'s row[number] to accommodate your source data. 
- <br/>
After that the script will print out the results in a txt file at the specified destination. 

