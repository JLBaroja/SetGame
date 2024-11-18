import os
import random
from flask import Flask, render_template
app = Flask(__name__)

deck_dir = 'static/cards/'
full_deck = os.listdir(deck_dir)

@app.route('/')
def game():
	initial_cards = random.sample(full_deck,12)
	card_urls = [f'/static/cards/{card}' for card in initial_cards]
	return render_template('frontend.html',cards=card_urls)

if __name__=='__main__':
	app.run(debug=True)

