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
    """Seu código deve vir aqui"""


NEWS = [
    {
        "url": "https://blog.betrybe.com/novidades/noticia_0.htm",
        "title": "noticia_0",
        "timestamp": "23/11/2020",
        "writer": "Escritor_0",
        "comments_count": 2,
        "summary": "Sumario da noticia_0",
        "category": "Categoria_0",
        "tags": ["PC_0", "Console_0"],
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-bacana",
        "title": "Notícia bacana",
        "writer": "Eu",
        "summary": "Algo muito bacana aconteceu",
        "comments_count": 4,
        "timestamp": "04/04/2021",
        "tags": ["Tecnologia", "Esportes"],
        "category": "Ferramentas",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia-legal",
        "title": "Notícia bacana 2",
        "writer": "Você",
        "summary": "Algo muito bacana aconteceu de novo",
        "comments_count": 1,
        "timestamp": "07/04/2022",
        "tags": ["Tecnologia"],
        "category": "Novidades",
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_3.htm",
        "title": "noticia_3",
        "timestamp": "23/11/2020",
        "writer": "Escritor_3",
        "comments_count": 1,
        "summary": "Sumario da noticia_3",
        "category": "Ferramentas",
        "tags": ["PC_3", "Console_3"],
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_4.htm",
        "title": "noticia_4",
        "timestamp": "23/11/2020",
        "writer": "Escritor_4",
        "comments_count": 1,
        "summary": "Sumario da noticia_4",
        "category": "Ferramentas",
        "tags": ["PC_4", "Console_4"],
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_5.htm",
        "title": "noticia_5",
        "timestamp": "23/11/2020",
        "writer": "Escritor_5",
        "comments_count": 1,
        "summary": "Sumario da noticia_5",
        "category": "Categoria_0",
        "tags": ["PC_5", "Console_5"],
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_6.htm",
        "title": "noticia_6",
        "timestamp": "23/11/2020",
        "writer": "Escritor_6",
        "comments_count": 1,
        "summary": "Sumario da noticia_6",
        "category": "Novidades",
        "tags": ["PC_6", "Console_6"],
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_7.htm",
        "title": "noticia_7",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "comments_count": 7,
        "summary": "Sumario da noticia_1",
        "category": "Categoria_7",
        "tags": ["PC_7", "Console_7"],
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_8.htm",
        "title": "noticia_8",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "comments_count": 8,
        "summary": "Sumario da noticia_8",
        "category": "Categoria_7",
        "tags": ["PC_7", "Console_6"],
    },
    {
        "url": "https://blog.betrybe.com/novidades/noticia_9.htm",
        "title": "noticia_9",
        "timestamp": "23/11/2020",
        "writer": "Escritor_7",
        "comments_count": 5,
        "summary": "Sumario da noticia_9",
        "category": "Categoria_9",
        "tags": ["PC_7", "Console_6"],
    },
]


# top_5_news(NEWS)

# Referências:
# 1- https://diegomariano.com/como-ordenar-um-dicionario-em-python/
