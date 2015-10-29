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
	response = {'polarity' : text.polarity , 'subjectivity' : text.subjectivity , 'nou' : text.tags}
	return jsonify(response)
	
@app.route('/api/v1/pos/<message>')
def pos(message):
	text = TextBlob(message)
	response = {'pos' : text.tags}
	return jsonify(response)
	
@app.route('/api/v1/lem/<message>')
def lem(message):
	text = Word(message)
	lem = text.lemmetize()
	lemv = text.lemmetize("v")
	response = {'lem' : lem, 'lemv' : lemv, 'defn' : text.definitions}
	return jsonify(response)


if __name__ == "__main__":
	app.run(debug=True)
