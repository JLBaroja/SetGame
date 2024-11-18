import os
import random

deck_dir = 'Cards/'
full_deck = os.listdir(deck_dir)
shuffled_deck = full_deck[:]
random.shuffle(shuffled_deck)

board = shuffled_deck[:12]
print(board)

select = input('Pick cards:')
int_sel = [int(x) for x in select.split()]
selected_cards = [board[i] for i in int_sel]

def is_set(cards):
	split_cards = [s.split('_') for s in cards]
	num_unique_values = [len(set([pos[dim] for pos in split_cards])) for dim in range(4)]
	return all(counts in {1,3} for counts in num_unique_values)
