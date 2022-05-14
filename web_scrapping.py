'''
grab image, title and price for all books which has rating 5 https://books.toscrape.com/
'''
import requests
import bs4
import re

def get_pager_max_range():
    result = requests.get("https://books.toscrape.com/catalogue/page-1.html")
    soup = bs4.BeautifulSoup(result.content.decode('utf-8'), "lxml")
    pager_text = soup.select('.pager .current')[0].text
    pagination_numbers = re.findall(r'\d+', pager_text)
    return int(pagination_numbers[1]) + 1

page_url = 'https://books.toscrape.com/catalogue/page-{}.html'
five_star_books = []

for page_num in range(1, get_pager_max_range()):
    print('fetching data from page {}...'.format(page_num))
    result = requests.get(page_url.format(page_num))
    soup = bs4.BeautifulSoup(result.content.decode('utf-8'), "lxml")
    books = soup.select('.product_pod')
    print('fetching books...')
    for book in books:
        if len(book.select('.star-rating.Five')) > 0:
            book_title = book.select('h3 a')[0]['title']
            book_image = book.select('.image_container img')[0]['src']
            book_price = book.select('.product_price .price_color')[0].text
            five_star_books.append((book_title, book_image, book_price))
    print('books saved from page {}...'.format(page_num))
        
for book in five_star_books:
    print(book)
    print("-" * 20)