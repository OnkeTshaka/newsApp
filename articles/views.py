from django.http import request
from django.shortcuts import render,redirect
from newsapi import NewsApiClient
from .models import Contact


# Create your views here.
def index(request):

   
    newsApi = NewsApiClient(api_key='a6d66a918fcf49a7902238dcdb2ae605')
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

    
def contact(request):
    name = request.POST['name']
    email =request.POST['email']
    subject =request.POST['subject']
    message =request.POST['message']

    contact = Contact.objects.create(Name=name, Email=email, Subject=subject,Message= message)
    contact.save()
    return render(request,'articles/index.html')


