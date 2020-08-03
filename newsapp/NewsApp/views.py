from django.shortcuts import render
from newsapi import NewsApiClient
# Create your views here.
def index(request):
    newsapi = NewsApiClient(api_key="faa255b9fa124dd4828f809a9a80f317")
    topheadlines = newsapi.get_top_headlines(sources="the-times-of-india")
    articles = topheadlines['articles']
    desc=[]
    news=[]
    img=[]
    for i in range(len(articles)):
        myarticle = articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])

    mylist = zip(news,desc,img)
    return render(request,'NewsApp/index.html',context={"mylist":mylist})

def bbc(request):
    newsapi = NewsApiClient(api_key="faa255b9fa124dd4828f809a9a80f317")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")
    articles = topheadlines['articles']
    desc=[]
    news=[]
    img=[]
    for i in range(len(articles)):
        myarticle = articles[i]
        news.append(myarticle['title'])
        desc.append(myarticle['description'])
        img.append(myarticle['urlToImage'])

    mylist = zip(news,desc,img)
    return render(request,'NewsApp/bbc.html',context={"mylist":mylist})

