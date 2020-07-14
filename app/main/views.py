from flask import render_template
from . import main
from ..request import get_news,get_headline
from ..news import News

# Views
@main.route('/')
def index():

    # Getting News articles fingers crossed
    sources_news = get_news()
    print(sources_news)
    title = 'Home - Welcome to LateLateMorning News - Keeps You Informed'
    return render_template('index.html',title = title, news_List = sources_news)

@main.route('/news/<news_id>')
def news(news_id):

    return render_template('news.html',id = news_id)

@main.route('/headline/<int:id>')
def headline(id):
    headline = get_headline(id)
    title = f'{headline.title}'
    return render_template('headline.html',title = title, headline=headline)


