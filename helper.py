"""

this file will manage the csv file only

store and retrieve data from here

"""
import csv
from results import *


"""
class resultsHelper():
    def importVotes(self):
    

        #Count the separate occurrences of votes.
        result = {}
        with open('votingrecords2.csv', 'r', newline='') as csv_file:
            csv_reader = csv.reader(csv_file)

            for line in csv_file:
                print(line[0])

    #return result


    def changeWinnerData(self):
        Ui_Results.retranslateUi().self.label_18.setText(str())



jv=1
ev=2
pv=3

class candidateMenuHelper():

    def logVote():
        with open('votingrecords.csv', 'w', newline='') as csv_file:
            fieldnames = ['Jeane', 'Edwin', 'Patricia']
            csv_reader = csv.reader(csv_file)
            csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            csv_writer.writeheader()
            csv_writer.writerow()

#candidateMenuHelper.logVote()



resultsHelper.importVotes()

"""

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
