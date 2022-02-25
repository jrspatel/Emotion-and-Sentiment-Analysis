


from flask import Flask,request,jsonify
import string
import nltk
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize



app = Flask(__name__)

result = {}

def sentiment_checker(sentence):
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer().polarity_scores(sentence)
    return sid

@app.route('/',methods = ['GET','POST'])
def sentiment_request():
    if request.method == 'POST':
        sentence = request.form['q']

        print('hello')

    else :
        sentence = request.args.get('q')
        print(request.args)
        print(sentence)

    sent = sentiment_checker(sentence)
    result['sentiment_checker'] = {'scores' : sent ,
                                 'senetence' : sentence}

    return jsonify(result)


if __name__=='__main__':
    app.run()






