import feedparser
import config

def get_news(url):
    news_feed = feedparser.parse(url)
    news = []
    entry = news_feed.entries

    for x in entry: 
        news.append(x.link) 

    return news