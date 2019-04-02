import requests
from flask import Flask, render_template

app = Flask(__name__)

API_KEY = '77e06fc676f04dcdbdf12b59a276f4f0'
NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={}'.format(API_KEY)

def get_news_articles():
    # fetch the news articles
    response = requests.get(NEWS_API_URL)

    # return the articles in json format
    return response.json()['articles']

@app.route("/")
def index():
    return str(get_news_articles())
