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

def preprocessing(text):
    text = text.lower()
    # removing punctuation
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))
    # tokenozing
    tokenize_words = cleaned_text.split()
    # removing stopwords
    stop_words = set(stopwords.words('english'))
    filtered_Sentence = [w for w in tokenize_words if not w.lower() in stop_words]

    return filtered_Sentence

def emotion_checker(sentence):
    emotion_list = []
    filtered_Sentence = preprocessing(sentence)
    with open('C:/Users/lenovo/PycharmProjects/testapi/testapi/emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace('\n', '').replace(',', '').replace("'", "").strip()
            word, emotion = clear_line.split(':')

            if word in filtered_Sentence:
                emotion_list.append(emotion)

@app.route('/',methods = ['GET','POST'])
def sentiment_request():
    if request.method == 'POST':
        sentence = request.form['q']

    else :
        sentence = request.args.get('q')

    emotions = emotion_checker(sentence)
    result['emotion_checker'] = {'emotions' : emotions ,
                                'senetence' : sentence}

    return jsonify(result)





if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 8080)