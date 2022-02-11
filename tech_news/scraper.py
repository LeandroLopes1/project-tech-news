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
    selector = parsel.Selector(html_content)

    url = selector.css(
        "link[rel='canonical'][href*='tecmundo.com.br/']::attr(href)").get()
    title = selector.css("h1.tec--article__header__title::text").get()
    timestamp = selector.xpath("//time[@id='js-article-date']/@datetime").get()
    writer = selector.css(".tec--author__info *:first-child *::text").get()
    if writer is None:
        writer = selector.css(
            "div.tec--timestamp__item.z--font-bold a::text").get()
    # https://stackoverflow.com/questions/34887730/how-to-extract-raw-html-from-a-scrapy-selector
    shares_count = selector.css(".tec--toolbar__item::text").re_first(r"\d+")
    comments_count = selector.css("svg.feather.z--mr-8::text").re_first(r"\d+")
    summary = selector.css(
        ".tec--article__body > p:first-child *::text").getall()
    sources = selector.css(
        ".z--mb-16 h2.z--text-base.z--font-semibold ~ div a.tec--badge::text"
        ).getall()
    categories = selector.css(
        "#js-categories a.tec--badge.tec--badge--primary::text").getall()

    listSources = []
    for source in sources:
        listSources.append(source.strip())

    listCategories = []
    for category in categories:
        listCategories.append(category.strip())

    return {
        'url': url,
        'title': title,
        'timestamp': timestamp,
        'writer': writer.strip() if writer else None,
        'shares_count': int(shares_count) if shares_count else 0,
        'comments_count': int(comments_count) if comments_count else 0,
        'summary': "".join(summary),
        'sources': listSources,
        'categories': listCategories
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
