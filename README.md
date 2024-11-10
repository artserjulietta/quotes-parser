# quotes-parser

Данный код парсит цитаты с сайта https://quotes.toscrape.com/ и генерирует из них JSON файл. Он состоит из списка цитат, где каждая цитата является словарем с тремя ключами:
1. "quote" : str (текст цитаты)
2. "author" : dict ```{ "name" : str (имя автора),
     "link" : str (ссылка на автора)}```
4. "tags" : list of dict ```{  "tag" : str (название тега),
      "link" : str (ссылка на тег)}```

Пример словаря с информацией о цитате:
```
{
        "quote": "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.",
        "author": {
            "name": "Albert Einstein",
            "link": "/author/Albert-Einstein"
        },
        "tags": [
            {
                "tag": "change",
                "link": "/tag/change/page/1/"
            }
        ]
}
```


    
