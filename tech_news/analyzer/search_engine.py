from tech_news.database import search_news
from datetime import datetime


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
    # Data no formato ISO AAAA-MM-DD
    # Referencia 2
    res = True
    search_list_tuple = []
    try:
        verify_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
        res = bool(verify_date)
    except ValueError:
        res = False
        raise ValueError("Data inválida")

    if (res is True):
        search_list = search_news(
            {"timestamp": {"$regex": verify_date, "$options": "i"}}
        )
        search_list_tuple = [
            tuple((search["title"], search["url"])) for search in search_list
        ]

    return search_list_tuple


# Requisito 8
def search_by_tag(tag):
    search_list = search_news({"tags": {"$regex": tag, "$options": "i"}})
    search_list_tuple = [
            tuple((search["title"], search["url"])) for search in search_list
        ]

    return search_list_tuple


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""


# Referencia:
# 1- https://www.delftstack.com/pt/howto/python/tuple-comprehension-python
# 2- https://acervolima.com/python-validar-formato-de-data-de-string/
