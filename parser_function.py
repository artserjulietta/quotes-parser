import requests
from bs4 import BeautifulSoup
import json

# Функция для парсинга цитат
def get_all_quotes(): 
    
    # Создаем пустой список, который будет являться результатом парсинга
    data = []
    # Цикл позволяет перебрать все страницы с цитатами (всего на сайте прдеставлено 10 страниц)
    for page in range(1,11):
        # Генерируеи ссылку, используя переменную page, которая хранит номер страницы
        url = f"https://quotes.toscrape.com/page/{page}/"
        # Отправляем запрос к API
        response = requests.get(url)
        # Проверка на то, что запрос к API прошел успешно
        if response.status_code == 200:
            # Собираем все цитаты со страницы, если что-то пойдет не так - вернем в результате сообщение с ошибкой 
            try:
                # Парсим страницу
                soup = BeautifulSoup(response.content, 'html.parser')
                # Находим все цитаты на странице
                quotes = soup.find_all('div', class_='quote')
                # Для каждой цитаты выделим необходимую информацию из тега div 
                for quote in quotes:
                    # Информация о каждой цитате будет храниться в отдельном словаре
                    quote_dict = {}
                    # Получаем текст цитаты и добавляем его в словарь по ключу "quote"
                    quote_text = quote.find('span', class_='text').get_text().strip('“”') # Используем strip('“”') для удаления лишних символов кавычек в начале и конце цитаты
                    quote_dict["quote"] = quote_text
                    # Получаем информацию об авторе (имя и ссылку) и добавляем его в словарь по ключу "author", в качестве значения будет словрарь с ключами "name" и "link" 
                    author_name = quote.find('small', class_='author').get_text() 
                    author_link = quote.find('a').get('href')
                    quote_dict["author"] = {
                                            'name' : author_name,
                                            'link' : author_link
                                            }
                    # Получаем теги цитаты и добавляем их в словарь по ключу "tags"
                    tags = quote.find_all('a', class_='tag')
                    tags = [{
                                "tag" : tag.get_text(), 
                                "link" : tag.get('href')
                             } 
                             for tag in tags]
                    quote_dict["tags"] = tags
                    # Добавляем получившийся словарь в итоговый список с данными
                    data.append(quote_dict)
            # Обрабатываем ошибку, которая может возникнуть в процессе парсинга
            except Exception as error:
                print(f"Произошла ошибка: {error}") 
        # Обрабатываем неудачный запрос к API
        else:
            print(f"Ошибка: Не удалось получить страницу. Код статуса: {response.status_code}")
    # Возвращаем список с цитатами
    return data


# Основной код
if __name__ == "__main__":
    # Получаем список всех дат в формате словарей
    all_quotes_data = get_all_quotes()
    # Записываем в файл quotes.json данные
    with open('quotes.json', 'w', encoding='utf-8') as f:
            json.dump(all_quotes_data, f, indent=4, ensure_ascii=False)
    print("Данные сохранены в файл quotes.json")
