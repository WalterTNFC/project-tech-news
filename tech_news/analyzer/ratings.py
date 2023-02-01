from typing import Counter
from tech_news.database import find_news


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    # Buscar a noticia
    search = find_news()
    # Calcular a popularidade:
    # Ordenar de forma crescente e pegar o maior valor
    # Referência 1
    sorted_list = sorted(
        search, key=lambda k: (k['comments_count'], k['title']), reverse=True
    )

    # Se tiver menos de cinco retornar o que tiver
    if len(sorted_list) <= 5:
        top_5_tuple = [
            tuple((search["title"], search["url"])) for search in sorted_list
        ]
        return top_5_tuple

    # Se tiver mais de 5:
    top_5 = []

    for i in range(5):
        top_5.append(sorted_list[i])

    top_5_tuple = [
            tuple((search["title"], search["url"])) for search in top_5
        ]

    return top_5_tuple


# Requisito 11
def top_5_categories():
    search = find_news()

    # Para ordenar e verificar mais recorrente
    categories = [result["category"] for result in search]
    sorted_categories = sorted(categories)
    count = Counter(sorted_categories)
    verify_most_common = count.most_common()

    top_5 = [category[0] for category in verify_most_common]

    return top_5


# Referências:
# 1- https://diegomariano.com/como-ordenar-um-dicionario-em-python/
