import os
import random
import itertools

def is_set(cards):
	split_cards = [s.split('_') for s in cards]
	num_unique_values = [len(set([pos[dim] for pos in split_cards])) for dim in range(4)]
	return all(counts in {1,3} for counts in num_unique_values)

def find_sets(board):
	combinations = list(itertools.combinations(board,3))
	are_sets = [is_set(comb) for comb in combinations]
	sets_indices = [i for i, val in enumerate(are_sets) if val]
	sets_found = [combinations[i] for i in sets_indices]
	return sum(are_sets), sets_found

deck_dir = 'Cards/'
full_deck = os.listdir(deck_dir)
shuffled_deck = full_deck[:]
random.shuffle(shuffled_deck)

board = shuffled_deck[:12]
print(board)

select = input('Pick cards:')
int_sel = [int(x) for x in select.split()]
selected_cards = [board[i] for i in int_sel]

print(is_set(selected_cards))
print(find_sets(board))




