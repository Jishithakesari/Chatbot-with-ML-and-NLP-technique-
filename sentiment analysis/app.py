from flask import Flask, request, render_template
from textblob import TextBlob
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict', methods=['POST'])
def predict():
   
    try:
        text = request.form['text']
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment > 0.5:
            response = 'Positive'
        elif sentiment < -0.5:
            response = 'Negative'
        else:
            response = 'Neutral'
    except Exception as e:
        print(e)
        response = 'Error: Please provide a valid input'
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
