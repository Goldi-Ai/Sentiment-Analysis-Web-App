from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', sentiment=None, text=None, polarity=None)

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        sentiment = 'Positive 😊'
    elif polarity < 0:
        sentiment = 'Negative 😢'
    else:
        sentiment = 'Neutral 😐'

    return render_template('index.html', sentiment=sentiment, text=text, polarity=round(polarity, 2))

if __name__ == '__main__':
    app.run(debug=True)
