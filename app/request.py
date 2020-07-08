from app import app
import urllib.request,json
from app.news import News



# Getting api key
api_key = app.config['NEWS_API_KEY']
print(api_key)
#Getting News base url
base_url = app.config["NEWS_API_SOURCE_URL"]
print(base_url)




def get_news():
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None
        
        if get_news_response['sources']:
            news_sources_list = get_news_response['sources']
            news_sources = process_sources(news_sources_list)
            print(get_news_url)
            print(news_sources)
           

    return news_sources




def process_sources(news_list):

    news_sources = []
    for news_item in news_list:

        id = news_item['id']
        name = news_item['name']
        description = news_item['description']
        url = news_item['url']
        category = news_item['category']
        language = news_item['language']
        country = news_item['country']

        if url:
            news_object = News(id,name,description,url,category,language,country)
            news_sources.append(news_object)
    
    return news_sources

def headline_source(id):
    headline_source_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id,api_key)
    print(headline_source_url)
    with urllib.request.urlopen(headline_source_url) as url:
        headline_source_data = url.read()
        headline_source_response = json.loads(headline_source_data)

        headline_source_results = None

        if headline_source_response['headline']:
            headline_source_list = headline_source_response['headline']
            headline_source_results = process_headline_results(headline_source_list)


    return headline_source_results


        



    
