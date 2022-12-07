"""

this file will manage the csv file only

store and retrieve data from here

once start another, rewrite the csv file.

testing
from welcom
if no data in csv, then raise exception
- try exept handler in controller

"""
import csv
from results import *
def logVote(vote_list):

    with open('votingrecords.csv', 'a', newline='') as csv_file:
        #fieldnames = ['Jeane', 'Edwin', 'Patricia']
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(vote_list)

def readVotes():
    CA_vote = 0
    CB_vote = 0
    CC_vote = 0

    with open('votingrecords.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            CA_vote += int(row[0].strip())
            CB_vote += int(row[1].strip())
            CC_vote += int(row[2].strip())

    return CA_vote, CB_vote, CC_vote

def main():
    var, var2, var3 = readVotes()


main()