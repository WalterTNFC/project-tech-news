import requests
from time import sleep
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    try:
        sleep(1)
        response = requests.get(
            url, headers={"user-agent": "Fake user agent"}, timeout=3
        )
        response.raise_for_status()
    except (requests.exceptions.HTTPError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    load_links = selector.css(".cs-overlay-link::attr(href)").getall()
    return load_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page = selector.css(".next::attr(href)").get()
    return next_page


def verifyFormat(text):
    import re
    remove = re.compile('<.*?>')
    return re.sub(remove, '', text)


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = len(selector.css("comment-list li").getall()) or 0
    summary = verifyFormat(selector.css(".entry-content p").get())
    tags = selector.css(".post-tags li a::text").getall()
    category = selector.css(".meta-category .label::text").get()

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary.strip(),
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    url = 'https://blog.betrybe.com/'
    links = []
    contador = 0

    while len(links) < amount:
        html_content = fetch(url)
        next_link = scrape_updates(html_content)

        try:
            request_page = fetch(next_link[contador])
            scrape = (scrape_news(request_page))
            links.append(scrape)
            contador = contador + 1
        except IndexError:
            url = scrape_next_page_link(html_content)
            contador = 0

    create_news(links)
    return links
