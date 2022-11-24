'''
Miguel Mayorga
CSCI 1620 fall 2022
lab 1_1
'''

def vote_menu():
    print('--------------------')
    print('VOTE MENU')
    print('--------------------')
    print('v - vote')
    print('x - exit')
    option = input('Option:').strip().lower()
    while option != "v" and option != "x":
        option = input('Invalid: (v\\x)').strip().lower()
    return option

def candidate_menu():
    print('--------------------')
    print('CANDIDATES')
    print('--------------------')
    print('0 - John')
    print('1 - Jane')
    vote = int(input('Candidate:'))
    while vote != 0 and vote != 1:
        vote = int(input('Invalid: (0\\1)'))
    return vote

def count_vote():

    canA_votes = 0
    canB_votes = 0
    totalVotes = canA_votes + canB_votes


    while True:

            temp_vote = vote_menu()
            if temp_vote == "x":
                break
            else:
                a = candidate_menu()
                canA_name = 'John'
                canB_name = 'Jane'
                if a == 0:
                    print(f'Voted {canA_name}')
                    canA_votes =  canA_votes + 1
                    totalVotes +=1
                elif a == 1:
                    print(f'Voted {canB_name}')
                    canB_votes += 1
                    totalVotes +=1
    print('--------------------')
    print(f'{canA_name} = {canA_votes}, {canB_name} = {canB_votes}, Total = {totalVotes}')


def main1():
    count_vote()

main()
