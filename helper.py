import csv
from results import *
from PyQt5 import QtWidgets

def logVote(vote_list):
    """
    adds the votes to the csv file

    :param vote_list: a list containing the votes
    :return: none
    """
    with open('votingrecords.csv', 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(vote_list)

def readVotes():
    """
    adds the votes to the csv file

    :param vote_list: a list containing the votes
    :return: none
    """
    CA_vote = 0
    CB_vote = 0
    CC_vote = 0
    # change filename to test error message
    with open('votingrecords.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader:
            CA_vote += int(row[0].strip())
            CB_vote += int(row[1].strip())
            CC_vote += int(row[2].strip())

    return CA_vote, CB_vote, CC_vote

def clearVotes():
    with open('votingrecords.csv', 'w', newline='') as csv_file:
        pass