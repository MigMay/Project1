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

def readVotes():
    CA_vote = 0
    CB_vote = 0
    CC_vote = 0

    with open('votingrecords2.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            CA_vote += int(row[0].strip())
            CB_vote += int(row[1].strip())
            CC_vote += int(row[2].strip())

        print(CA_vote)
        print(CB_vote)
        print(CC_vote)

    return CA_vote, CB_vote, CC_vote


def logVote():
    with open('votingrecords.csv', 'w', newline='') as csv_file:
        fieldnames = ['Jeane', 'Edwin', 'Patricia']
        csv_reader = csv.reader(csv_file)
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        csv_writer.writeheader()
        csv_writer.writerow()

def main():
    var, var2, var3 = readVotes()

main()