from flask import render_template
from app import app
from .request import get_news,headline_source

# Views
@app.route('/')
def index():

    # Getting News articles fingers crossed
    sources_news = get_news()
    print(sources_news)
    title = 'Home - Welcome to LateLateMorning News - Keeps You Informed'
    return render_template('index.html',title = title, news_List = sources_news)

@app.route('/news/<news_id>')
def news(news_id):

    return render_template('news.html',id = news_id)

@app.route('/headline/<id>')
def headline(id):
    headline = headline_source(id)
    return render_template('headline.html', headline=headlines,id=id) 



    
