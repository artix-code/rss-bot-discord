import feedparser
import config

# парсим RSS
def get_news(url):
    news_feed = feedparser.parse(url)
    news = []
    # переменная для все новостей
    entry = news_feed.entries

    for x in entry: 
        news.append(x.link) 

    return news

get_news(config.NEWS_URL)