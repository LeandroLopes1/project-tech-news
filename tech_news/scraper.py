import requests
import time
import parsel


# Requisito 1
def fetch(url):
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
        if response.status_code == 200:
            return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    urlNoticias = []
    for noticia in selector.css('div.tec--list__item'):
        urlNoticias.append(noticia.css('a::attr(href)').get())
    return urlNoticias


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    next_page = selector.css("a[href*='novidades?page=']::attr(href)").get()
    return next_page


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
