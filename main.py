#!/usr/bin/python3

import requests
from xml.dom.minidom import parseString
from htmldom import htmldom
import libgenapi
import time
import json

def get_toread_books_from_page(params):
    response = requests.get("https://www.goodreads.com/review/list", data=params)
    xml = parseString(response.content)

    total = int(xml.getElementsByTagName('reviews')[0].getAttribute('total'))
    all_books = xml.getElementsByTagName('book')

    my_isbn_list = []
    for book in all_books:
        book_isbn = {}
        book_isbn['title'] = book.getElementsByTagName('title')[0].firstChild.nodeValue

        old_isbn = book.getElementsByTagName('isbn')
        new_isbn = book.getElementsByTagName('isbn13')

        if (not old_isbn[0].hasAttribute('nil')):
            book_isbn['isbn'] = old_isbn[0].firstChild.nodeValue

        if (not new_isbn[0].hasAttribute('nil')):
            book_isbn['isbn13'] = new_isbn[0].firstChild.nodeValue
            
        if (len(book_isbn) > 0):
            my_isbn_list.append(book_isbn)
        else:
            print("The book \"%s\" has no ISBN." % book.getElementsByTagName('title')[0].firstChild.nodeValue)
    return [my_isbn_list, total]

def find_download_link_by_isbn(isbn):
    results = lg.search(isbn, "identifier")
    for result in results:
        if ((result['extension'] == 'epub') or (result['extension'] == 'mobi')):
            print("Encontrou!")
            mirror = result['mirrors'][0]
            dom = htmldom.HtmlDom("http://libgen.io" + mirror).createDom()
            h2s = dom.find('h2')
            for h2 in h2s:
                if (h2.text().lower() == "download"):
                    return [h2.parent().attr('href'), result['extension']]

def download_book(url, filename):
    with open(filename, "wb") as handle:
        print("Baixando arquivo...")
        response = requests.get("http://libgen.io" + url, stream=True)

        if not response.ok:
            return False

        for block in response.iter_content(1024):
            handle.write(block)
        return True

# Get "to-read" books from GoodReads.com
data = {
    'v': '2',
    'key': '<DEVELOPER_KEY>',
    'id': '<YOUR_DESIRED_ID>',
    'shelf': 'to-read',
    'per_page': 200,
    'page': 1
}
isbn_list = []

response = get_toread_books_from_page(data)
print(response[0])
isbn_list = response[0]
number_of_pages = response[1] / data['per_page']

# If there's more than 200 books, call GoodReads API more times.
if (number_of_pages > 1):
    for i in range(0, int(str(number_of_pages)[:1])):
        time.sleep(1)
        data['page'] = data['page'] + 1
        isbn_list = isbn_list + get_toread_books_from_page(data)[0]

print(isbn_list)

# Download books by ISBN from Libgen.io
lg=libgenapi.Libgenapi(["http://libgen.io/", "http://gen.lib.rus.ec/", "http://libgen.net/", "http://bookfi.org/"])
for isbn in isbn_list:

    time.sleep(1)

    # Trying to download via ISBN
    if 'isbn' in isbn:
        download_url = find_download_link_by_isbn(isbn['isbn'])
        if download_url:
            status = download_book(download_url[0], "downloads/" + isbn['title'] + "." + download_url[1])
            if (status):
                continue

    # Trying to download via ISBN13
    if 'isbn13' in isbn:
        download_url = find_download_link_by_isbn(isbn['isbn13'])
        if download_url:
            status = download_book(download_url[0], "downloads/" + isbn['title'] + "." + download_url[1])
            if (status):
                continue
        