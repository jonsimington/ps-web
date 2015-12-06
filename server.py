from flask import Flask, jsonify
import nltk
from nltk.corpus import brown
import json
import markovify
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/gen-sentence/<number>/<complexity>', methods=['GET'])
def get_sentence(number, complexity):
    global liked_sentences
    global book_text
    global text_model

    sentences = []
    
    for i in range(int(number)):
        sentences.append(text_model.make_short_sentence(int(complexity)))
        
    return json.dumps(sentences)

@app.route('/like/<sentence>', methods=["GET"])
def like_sentence(sentence):
    global liked_sentences

    if sentence not in liked_sentences:
        liked_sentences.append(sentence)

        # really return some code that the client uses to display a thanks popup
        return liked_sentences[len(liked_sentences) - 1]

    else:
        return "That one is already liked!"

if __name__ == '__main__':
    book_file_ids = ['austen-emma.txt', 'austen-persuasion.txt', 'austen-sense.txt',
                     'blake-poems.txt', 'bryant-stories.txt', 'burgess-busterbrown.txt',
                     'carroll-alice.txt', 'chesterton-ball.txt', 'chesterton-brown.txt',
                     'chesterton-thursday.txt', 'edgeworth-parents.txt', 'melville-moby_dick.txt',
                     'milton-paradise.txt', 'whitman-leaves.txt']

    liked_sentences = [""]
    book_text = ""

    for book in book_file_ids:
        book_text += nltk.corpus.gutenberg.raw(book)

    text_model = markovify.Text(book_text)

    app.run(debug=True, host='0.0.0.0', port=5000)
