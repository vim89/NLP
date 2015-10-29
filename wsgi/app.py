from flask import Flask , jsonify, render_template
from textblob import TextBlob
from textblob import Word

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/api/v1/sentiment/<message>')
def sentiment(message):
	text = TextBlob(message)
	response = {'polarity' : text.polarity , 'subjectivity' : text.subjectivity }
	return jsonify(response)
	
@app.route('/api/v1/lemm/<word>')
def lemm(word):
	text = Word(word)
	response = {'lresponse' : text.lemmatize()}
	return jsonify(response)

if __name__ == "__main__":
	app.run(debug=True)
