from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient


# Create your views here.
def index(request):

   
    newsApi = NewsApiClient(api_key='add api key')
    headLines = newsApi.get_top_headlines(sources='news24')
    articles = headLines['articles']
    desc = []
    news = []
    img = []
    ul =[]

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        ul.append(article['url'])
        news.append(article['title'])
        img.append(article['urlToImage'])
    mylist = zip(news, desc, img, ul)
    return render(request,'articles/index.html', context={"mylist": mylist})

    


