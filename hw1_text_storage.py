index_tasks = {
    "tasks": [
        {"task": "Задание 7",
         "description": """Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
Данные о новостях должны быть переданы в шаблон через контекст."""},
        {"task": "Задание 8",
         "description": """Создать базовый шаблон для всего сайта, содержащий общие элементы дизайна 
(шапка, меню, подвал), и дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты", используя базовый шаблон."""},
        {"task": "Задание 9",
         "description": """Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна 
(шапка, меню,подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон."""},
    ],
}

about_text = {
    "title": "Страница о нас",
    "about": "Самая лучшая компания",
}

contacts_text = {
    "title": "Контакты",
    "github": "https://github.com/KassandraKox",
}

news_content = {
    "title": "Новости",
    "news": [
        {"news_title": "Первая новость",
         "news_body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero, voluptates?",
         "date": "08 Августа 2023г."},
        {"news_title": "Вторая новость",
         "news_body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero, voluptates?",
         "date": "08 Августа 2023г."},
        {"news_title": "Третья новость",
         "news_body": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Libero, voluptates?",
         "date": "08 Августа 2023г."},
    ],
}

store_categories = {
    "title": "Магазин",
    "categories": [
        {"name": "Верхняя одежда",
         "link": "/store/outwears/"},
        {"name": "Обувь",
         "link": "/store/shoes/"},
        {"name": "Головные уборы",
         "link": "/store/hats/"},
    ]
}

store_pages = {
    "outwears": {
        "title": "Верхняя одежда",
        "products": [
            {"name": "Куртка",
             "price": "$100"},
            {"name": "Пальто",
             "price": "$150"},
            {"name": "Ветровка",
             "price": "$60"},
        ],
    },
    "shoes": {
        "title": "Обувь",
        "products": [
            {"name": "Кросовки",
             "price": "$50"},
            {"name": "Кеды",
             "price": "$35"},
            {"name": "Туфли",
             "price": "$60"},
        ],
    },
    "hats": {
        "title": "Головные уборы",
        "products": [
            {"name": "Федора",
             "price": "$100"},
            {"name": "Кепка",
             "price": "$15"},
            {"name": "Шапка",
             "price": "$20"},
        ],
    },
}