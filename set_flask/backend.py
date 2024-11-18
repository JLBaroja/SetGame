import os
import random
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

deck_dir = 'static/cards/'
full_deck = os.listdir(deck_dir)
initial_cards = random.sample(full_deck,12)

@app.route('/')
def game():
	#initial_cards = random.sample(full_deck,12)
	card_urls = [f'/static/cards/{card}' for card in initial_cards]
	print(card_urls)
	return render_template('frontend.html',cards=card_urls)

@app.route('/select_cards',methods=['POST'])
def select_cards():
	# Selected cards URLs from frontend
	selected_cards = request.json.get('selectedCards')
	print('Selected cards:',selected_cards)
	print(type(selected_cards))
	print(type(selected_cards[0]))
	#print('Selected cards:',initial_cards[selected_cards])
	return jsonify({'message':'Cards received!'})

if __name__=='__main__':
	app.run(debug=True)

