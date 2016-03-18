
final_tally = {'Al': 0, 'Bob': 0, 'Joan': 0}

print('Do you wish to begin? ')
voter_initial_answer = input()

print("- -" * 15)

while voter_initial_answer != 'Finalize':
    print('Choose Candidate: Al, Bob, Joan or choose Finalize: ')
    voter_initial_answer = input()
    if voter_initial_answer != 'Finalize':
        old_candidates_tally = final_tally[voter_initial_answer]
        new_candidates_tally = old_candidates_tally + 1
        final_tally[voter_initial_answer] = new_candidates_tally
    else:
        print (final_tally)

#to create a list made up of tuples which are the pairs of the \
#original dictionary items:

print('*' * 20)

#final_tally_list = final_tally.items()

#print(final_tally_list)

al_vote_count = int(final_tally['Al'])
bob_vote_count = int(final_tally['Bob'])
joan_vote_count = int(final_tally['Joan'])


#can the below use a for loop in some way to clean it up?

if al_vote_count > bob_vote_count and al_vote_count > joan_vote_count:
    print("Al is the winner with {} total votes!".format(al_vote_count))
elif bob_vote_count > al_vote_count and bob_vote_count > joan_vote_count:
    print("Bob is the winner with {} total votes!".format(bob_vote_count))
elif joan_vote_count > al_vote_count and joan_vote_count > bob_vote_count:
    print("Joan is the winner with {} total votes!".format(joan_vote_count))

print('*' * 20)

#max_of_final_tally = max(final_tally.values())
#final_name = final_tally.get(key, max_of_final_tally)

#print(max_of_final_tally)
#print(final_name)

#winner = final_tally_list.index(max_of_final_tally)

#find the index of the element in final_tally_list which contains the value from max_of_final_tally\
    #take that index, and get the index[1] from that indexed element

print('*' * 20)

#print(final_tally_list[winner[1]])
