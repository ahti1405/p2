import requests
from bs4 import BeautifulSoup


word = 'Помидоры (свежие)'
url = 'https://fitaudit.ru/food'


def get_html_page(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml') 
    return soup
    

def get_data(word):
    html = get_html_page(url)
    url2 = html.find('a', title=word)['href']
    html_page = get_html_page(url2)
    p = html_page.find('p', class_='him_bx__wrap')
    data = p.find_all('span', class_='js__msr_cc')

    calories = int(data[-6].text.split()[0])
    jiry = float(data[-5].text.split()[0].replace(',', '.'))
    belki = float(data[-4].text.split()[0].replace(',', '.'))
    uglevody = float(data[-3].text.split()[0].replace(',', '.'))
    voda = float(data[-2].text.split()[0].replace(',', '.'))
    zola = float(data[-1].text.split()[0].replace(',', '.'))

    # output = [calories, jiry, belki, uglevody, voda, zola]
    output = {
        'calories': calories,
        'jiry': jiry,
        'belki': belki,
        'uglevody': uglevody,
        'voda': voda,
        'zola': zola
    }
    return output
