import requests
from selectolax.parser import HTMLParser
import sqlite3


def get_games():
    games = {}
    games['game_title'] = data


def check_database():
    connection = sqlite3.connect('../Parser_steam/game_strategy.db')
    cursor = connection.cursor()
    f = open('data.txt', encoding='utf-8')
    new_data = []
    for item in f:
        new_data.append(item)
    for i in new_data:
        cursor.execute("""
            SELECT game_title FROM games_steam WHERE game_title = (?)
        """, (i,))

    result = cursor.fetchone()
    print(result)
    if result is None:
        for i in range(0, len(new_data)):
            cursor.execute("""
                INSERT INTO games_steam
                VALUES (NULL, :game_title)
                """, [new_data[i]])
            connection.commit()
    connection.close()


def get_html(url):
    response = requests.get(url=url)
    html = response.text
    tree = HTMLParser(html)
    items = tree.css('.title')
    index = 0
    data = []
    for item in items:
        index += 1
        x = item.css_first('span').text()
        data.append(x)

    f = open('data.txt', 'w', encoding='utf-8')
    for index in data:
        f.write(index + '\n')
    f.close()


def main():
    url = 'https://store.steampowered.com/search/?term=strategy&supportedlang=english&ndl=1'

    check_database()
    '''connection = sqlite3.connect('game_strategy.db')
    cursor = connection.cursor()
    cursor.execute ("""
        CREATE TABLE games_steam(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            game_title TEXT
        )
    """)
    connection.close()'''


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
