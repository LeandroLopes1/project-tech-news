from tech_news.database import search_news
import datetime


# Requisito 6
def search_by_title(title):
    # https://data-flair.training/blogs/mongodb-regular-expression-regex/
    title_news = search_news({"title": {"$regex": title, "$options": "i"}})
    list_news = []
    for news in title_news:
        list_news.append((news["title"], news["url"]))
    return list_news


# Requisito 7
def search_by_date(date):
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
    date_news = search_news({"timestamp": {"$regex": date}})
    list_news = []
    for news in date_news:
        list_news.append((news["title"], news["url"]))
    return list_news


# Requisito 8
def search_by_source(source):
    source_news = search_news({"sources": {"$regex": source, "$options": "i"}})
    list_news = []
    for news in source_news:
        list_news.append((news["title"], news["url"]))
    return list_news


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
