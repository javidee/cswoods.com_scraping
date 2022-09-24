import requests
from bs4 import BeautifulSoup
import pandas as pd

data = []

urls = ['https://cswoods.com/collections/finished-surfaces/products/bookmatched-eucalyptus-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/mesquite-bookmatch-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/hackberry-bookmatch-table-top', 'https://cswoods.com/collections/finished-surfaces/products/sycamore-bookmatch-table-top', 'https://cswoods.com/collections/finished-surfaces/products/black-root-base-coffee-table',
        'https://cswoods.com/collections/finished-surfaces/products/hackberry-traditional-table-top', 'https://cswoods.com/collections/finished-surfaces/products/black-walnut-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/hackberry-bookmatch-table-top-1', 'https://cswoods.com/collections/finished-surfaces/products/black-walnut-desk-top', 'https://cswoods.com/collections/finished-surfaces/products/black-walnut-bookmatch-table-top',
        'https://cswoods.com/collections/finished-surfaces/products/mango-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/cherry-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/elm-desk-top-1', 'https://cswoods.com/collections/finished-surfaces/products/sassafras-traditional-table-top-for-four', 'https://cswoods.com/collections/finished-surfaces/products/black-walnut-round-table-top',
        'https://cswoods.com/collections/finished-surfaces/products/iroko-coffee-table',
        'https://cswoods.com/collections/finished-surfaces/products/cherry-dining-table-top', 'https://cswoods.com/collections/finished-surfaces/products/kentucky-coffee-bean-traditional-table-top-for-four', 'https://cswoods.com/collections/finished-surfaces/products/kentucky-coffee-bean-traditional-table-top-for-four-1', 'https://cswoods.com/collections/finished-surfaces/products/eastern-white-pine-dining-table-2047',
        'https://cswoods.com/collections/finished-surfaces/products/american-elm-sit-stand-desktop', 'https://cswoods.com/collections/finished-surfaces/products/claro-walnut-9-bookmatched-table', 'https://cswoods.com/collections/finished-surfaces/products/desert-iron-wood-environmental-art', 'https://cswoods.com/collections/finished-surfaces/products/silver-maple-burl-coffee-table',
        'https://cswoods.com/collections/finished-surfaces/products/black-walnut-table-desk-top', 'https://cswoods.com/collections/finished-surfaces/products/red-oak-sit-stand-desk', 'https://cswoods.com/collections/finished-surfaces/products/black-walnut-bookmatch-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/maple-burl-table',
        'https://cswoods.com/collections/finished-surfaces/products/pond-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/african-mahogany-sipo-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/black-walnut-dining-table-1', 'https://cswoods.com/collections/finished-surfaces/products/claro-walnut-desk-2098',
        'https://cswoods.com/collections/finished-surfaces/products/iroko-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/claro-walnut-burl-coffee-table', 'https://cswoods.com/collections/finished-surfaces/products/american-single-slab-black-walnut-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/claro-walnut-10-6-bookmatched-table',
        'https://cswoods.com/collections/finished-surfaces/products/black-walnut-sit-stand-desk', 'https://cswoods.com/collections/finished-surfaces/products/bookmatched-black-walnut-dining-table', 'https://cswoods.com/collections/finished-surfaces/products/nutmeg-stump-coffee-table-2079']
for n in range(1, len(urls)):
    try:
        url = (urls[n])
    except:
        pass
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')


    link = url
    name = soup.find('div', class_='detail layout-column-half-right').find('h1', class_='title').text
    price = soup.find('span', class_='price theme-money').text
    description = soup.find('div', class_='description user-content').text
    mImage = soup.find('div', class_='gallery gallery-layout-beside layout-column-half-left has-thumbnails').find('a', class_='shows-lightbox').get('href')
    Images = [mImage]
    try:
        for i in range(1, 15):
            tImages = soup.find('div', class_='thumbnails').findAll('a', class_='')[i].get('href')
            Images.append(tImages)
    except:
        pass

    data.append([link, name, price, description, Images])

header = ["Посилання",'Назва', "Ціна", "Опис", "Зображення"]
df = pd.DataFrame(data, columns=header)
df.to_csv('D:\Tables.csv', sep=';', encoding='utf-8-sig')
print(link, name, price, description, Images)