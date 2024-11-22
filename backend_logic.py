import os
import random
import itertools
import time

def is_set(cards):
	split_cards = [s.split('_') for s in cards]
	num_unique_values = [len(set([pos[dim] for pos in split_cards])) for dim in range(4)]
	return all(counts in {1,3} for counts in num_unique_values)

def find_sets(board):
	combinations = list(itertools.combinations(board,3))
	are_sets = [is_set(comb) for comb in combinations]
	sets_indices = [i for i, val in enumerate(are_sets) if val]
	sets_found = [combinations[i] for i in sets_indices]
	
	return {
		'number_sets':sum(are_sets),
		'sets_in_board':sets_found}

deck_dir = 'Cards/'
full_deck = os.listdir(deck_dir)
shuffled_deck = full_deck[:]
random.shuffle(shuffled_deck)


set_game = {}
disp_counter = 1
deck_position = 12
board = shuffled_deck[:deck_position]
deck_remaining = shuffled_deck[deck_position:]
rep=True
while rep:
	
	# Print board
	board_label = 'Trial'+str(disp_counter)
	print('\n'+board_label)
	[print(i) for i in board]
	
	# Time
	trial_start = time.time()

	# Print sets (testing only)
	display = find_sets(board)
	print(display)
	if display['number_sets']!=0:
		set_pos=[indx for indx, value in enumerate(board) if value in display['sets_in_board'][0]]
		print(set_pos)

	print('Cards remaining '+str(len(deck_remaining)))

	if len(deck_remaining)==0 and display['number_sets']==0:
		print('Game Over!')
		break
	else:
	  # Store Data 
		set_game[board_label]={
			'board':board,
			'number_sets':display['number_sets'],
			'sets_in_board':display['sets_in_board']}
		
		# User input
		select = input('Pick cards:').split()
		if select[0] == 'more': # MORE cards
			if display['number_sets']==0:
				print('You got me dude!')
	      # Correct More
				disp_counter=disp_counter+1
				if len(deck_remaining)>0:
					board.extend(deck_remaining[:3])
					deck_remaining=deck_remaining[3:]
			else:
				print('There\'s at least one set!') 
				# Mistake More
		else: # THREE cards selected
			int_sel = [int(x) for x in select]
			selected_cards = [board[i] for i in int_sel]	
			# Evaluate selextion
			if is_set(selected_cards):
				print('That\'s a set!')
				# Correct Set
				disp_counter=disp_counter+1
				# Eliminate set from display
				board = [x for i, x in enumerate(board) if i not in int_sel]
				# Update board
				if len(deck_remaining)>0 and len(board)==9:
					board.extend(deck_remaining[:3])
					deck_remaining=deck_remaining[3:]
			else:
				print('That ain\'t no set!')
				# Mistake Set

