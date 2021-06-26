import flask
from flask import Flask, request, session, redirect, url_for, render_template
import re  
import nltk
from nltk.corpus import stopwords
from heapq import nlargest
import spacy
import txtai
import time
from txtai.pipeline import Summary

STOP_WORDS = set(stopwords.words('english')) 
stopwords = list(STOP_WORDS)
nlp = spacy.load('en_core_web_sm')

app = Flask(__name__,static_url_path='/static')

@app.route('/')
def homepage():
    return render_template('index.html')





@app.route('/JD', methods=['GET','POST'])
def JD():
    sumup=''
    summary1=''
    output_sum=''
    summary2=''
    len_text=''
    text=''
    outcome=''
    display_text = {}
    if request.method == 'POST':
        from string import punctuation
        from txtai.pipeline import Summary
        summary = Summary()
        text = request.form['text']
        outcome = long_load(text)
        text_length = len(text)
        doc = nlp(text)
        tokens = [token.text for token in doc]
        punctuation = punctuation + '\n'
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word]/max_frequency
        sentence_tokens = [sent for sent in doc.sents]
        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]

        select_length = int(len(sentence_tokens)*0.5)



        summary1 = nlargest(select_length, sentence_scores,
                            key=sentence_scores.get)
        sumup=summary(summary1[0])
        k=''

        k="The Summarized Version is:"

        
        # sumup = summary(text)
        # sumup=sumup



  
        

    return render_template('index.html',sumup=sumup,k=k)




if __name__ == '__main__':
    app.run(debug=True)
