
import urllib.request,json
from app.news import News

# Getting api key
api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    print(api_key)
    base_url = app.config["NEWS_API_SOURCE_URL"]
    print (base_url)





def get_news():
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_sources = None
        
        if get_news_response['articles']:

            news_sources_list = get_news_response['articles']
            news_sources = process_sources(news_sources_list)
           
           

    return news_sources




def process_sources(news_list):

    news_sources = []
    for news_item in news_list:
    
        id = news_item['source']['id']
        name = news_item['source']['name']
        title = news_item['title']
        author = news_item['author']
        description = news_item['description']
        url = news_item['url']
        urlToImage = news_item ['urlToImage']
        publishedAt = news_item ['publishedAt']
        content = news_item['content']

        if url:
            news_object = News(id,name,title,author,description,url,urlToImage,publishedAt,content)
            news_sources.append(news_object)
    
    return news_sources

def get_headline():
    get_headline_url = base_url.format(api_key)

    with urllib.request.urlopen(get_headline_details_url) as url:
        headline_details_data = url.read()
        headline_details_response = json.loads(headline_details_data)
        headline_object = None
        if headline_details_response:
             id = news_item('id')
             name = news_item('name')
             description = news_item('description')
             url = news_item('url')
             category = news_item('category')
             language = news_item('language')
             country = news_item('country')

             headline_object = Headline(id.name,description,url,category,language,country)

        return headline_object





        



    
