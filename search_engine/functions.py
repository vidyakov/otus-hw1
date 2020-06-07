import json
import csv
from requests import get


from bs4 import BeautifulSoup


def _save_page(page, filename):
    with open(f'{filename}.html', 'w', encoding='utf-8') as file:
        file.write(page)


def get_search_request(text: str, machine: str) -> str:
    if machine == 'yandex.ru':
        url = 'https://yandex.ru/search/'
        request = get(url, params={'text': text, 'lr': 213})
    else:
        url = 'https://google.com/search'
        request = get(url, params={'q': text.replace(' ', '+')})
    # _save_page(request.text, machine)
    return request.text


def get_simple_request(url: str):
    request = get(url)
    return request.text


def get_links(page: str, quantity: int = 5, machine: str = None) -> [] or str:
    soup = BeautifulSoup(page, 'html.parser')

    if machine == 'yandex.ru':
        elements = soup.find_all(class_='organic__url', limit=quantity)
        links = list(map(lambda elem: elem['href'], elements))
        return links
    elif machine == 'google.com':
        elements = soup.find_all('a', limit=quantity + 35)
        links = list(map(lambda elem: elem, elements))[36:]
        return list(filter(lambda link: link is not None, links))
    else:
        elements = soup.find_all('a')
        for element in elements:
            link = element.get('href')
            if link is not None:
                return link


def save_in_json(links):
    with open('links.json', 'w', encoding='utf-8') as json_file:
        json.dump(links, json_file)


def save_in_csv(links):
    with open('links.csv', 'w', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(links)
