from flask import Flask
import requests


app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 align='center'>Welcome to News API</h1>"
@app.route('/news')
def news():
    API_KEY = '0e672bdff5f34651a87b002e9b71b127'
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']
    news = []
    for article in articles:
        news_dict = {
            'source': article['source']['name'],
            'title': article['title'],
            'description': article['description'],
            'url': article['url'],
            'published_at': article['publishedAt']
        }
        news.append(news_dict)
    return news

@app.route('/quit')
def quit():
    return "<h1 align='center'>Good Bye</h1>"


if __name__ == '__main__':
    app.run()


