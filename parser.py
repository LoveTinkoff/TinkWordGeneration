'''Это парсер, именно благодаря этой программе я получил текстовый файл в котором были 7 книг из цикла
Стивена кинга: "Темная Башня". Программа можем запихать в текстовый файл сразу несколько книг, для
этого нужно указать требуемое кол-во книг, затем для каждой указать ссылку на ее первую страницу
и количество страниц в ней. Данные берутся с сайта http://www.studynovels.com/
 P.S. Программа общается с пользователем, вводить данные нужно по мере их надобности'''

import requests
from bs4 import BeautifulSoup
from time import perf_counter

HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
HOST = 'http://www.studynovels.com/'
URL = 'http://www.studynovels.com/Page/Story?bookId=5650&pageNo=1'

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    ans = ''
    pred = soup.find('div', class_='card-body').find_all('p')
    for elem in pred:
        ans += elem.get_text()
    return ans

def parse(URL, num):
    URL = URL[:-1]
    ans = ''
    for i in range(1, num + 1):
        URL1 = URL + str(i)
        html = get_html(URL1)
        ans += get_content(html.text)
    return ans

f = open('DARK_TOWERS.txt', 'w')
print('Здравствуйте, это парсер сайта http://www.studynovels.com/. Введите желаемое количество книг : ')
n = int(input())
result = ''
for i in range(1, n + 1):
    print('введите ссылку на первую страницу ', i, ' книги : ')
    URL = input()
    print('страниц в книге : ')
    m = int(input())
    start_time = t1_start = perf_counter()
    result += parse(URL, m)
    stop_time = perf_counter()
    print('Успешно! ', "{:g} s".format(stop_time - start_time))
f.write(result)


