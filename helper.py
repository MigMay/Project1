"""

this file will manage the csv file only

store and retrieve data from here

"""

import csv

import


class resultsHelper():
    def importVotes(self):
        pass

    def changeWinnerData(self):


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

candidateMenuHelper.logVote()
