from flask import Flask , jsonify, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/api/v1/sentiment/<message>')
def sentiment(message):
	text = TextBlob(message)
	response = {'polarity' : text.polarity , 'subjectivity' : text.subjectivity}
	return jsonify(response)
	
@app.route('/api/v1/pos/<message>')
def pos(message):
	text = TextBlob(message)
	response = {'pos' : text.tags, 'nou' : text.noun_phrases}
	return jsonify(response)
	
@app.route('/api/v1/langtrans/<message>')
def langtrans(message):
	text = TextBlob(message)
	response = {'french' : str(text.translate(to='fr')), 'spanish' : str(text.translate(to='es'))}
	return jsonify(response)
	
@app.route('/api/v1/spellcheck/<message>')
def spellcheck(message):
	text = TextBlob(message)
	response = {'crt' : str(text.correct())}
	return jsonify(response)

if __name__ == "__main__":
	app.run(debug=True)
