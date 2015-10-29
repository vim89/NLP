from flask import Flask , jsonify, render_template
from textblob import TextBlob
from subprocess import Popen, PIPE

p = Popen('curl https://raw.github.com/sloria/TextBlob/master/download_corpora.py | python', shell=True,
          stdout=PIPE, stderr=PIPE)
out, err = p.communicate()

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

if __name__ == "__main__":
	app.run(debug=True)
