from flask import Flask, jsonify
from book_text import book_text
import nltk
from nltk.corpus import brown
import json
from markovgen import Markov

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/<genres>', methods=['GET'])
def get_sentence(genres):
    genre_list = genres.split()

    brown_text = [' '.join([x for x in brown.words(categories=genre_list) if x not in ['?', ',', '"', '""', "'", "''", '`', '``', '!']])]
    markov = Markov(brown_text).generate_markov_text(backward=True)
    print("markov: ", markov)
    return markov
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
