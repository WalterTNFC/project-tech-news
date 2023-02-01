from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    # Recebe uma string
    # Buscar pelo titulo
    # Retornar uma lista de tuplas
    # Referência: [1]
    search_list = search_news({"title": {"$regex": title, "$options": "i"}})
    search_list_tuple = [
        tuple((search["title"], search["url"])) for search in search_list
    ]

    return search_list_tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# Referencia:
# 1- https://www.delftstack.com/pt/howto/python/tuple-comprehension-python
