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




        



    
