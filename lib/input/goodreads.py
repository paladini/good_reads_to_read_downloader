import requests
from xml.dom.minidom import parseString
from htmldom import htmldom
import time
import json

# Loading modules in parent folders
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from misc.book import Book

class GoodReads(object):

    def __init__(self, api_options):
        self.api_options = api_options
        self.options = self.get_statistics()

    def __init__(self, key, user_id, shelf='to-read', per_page=200, page=0, version='2'):
        self.api_options = {
            'v': str(version),
            'key': str(key),
            'id': str(user_id),
            'shelf': str(shelf),
            'per_page': int(per_page),
            'page': int(page)
        }
        self.options = self.get_statistics()

    def get_books(self, from_page=0, to_page=None):
        isbn_list = []

        # If "to_page" wasn't provided, then retrieve all books.
        if (to_page is None): to_page = self.options['total_pages']

        for page in range(int(from_page), int(to_page)):

            # Making the API call for the current page
            self.api_options['page'] = page
            time.sleep(1) # the sleep is needed because GoodReads API limitations.
            response = requests.get("https://www.goodreads.com/review/list", data = self.api_options)
            xml = parseString(response.content)
            xml_books = xml.getElementsByTagName('book')
            
            for xml_current_book in xml_books:

                # print(xml_current_book)

                # Getting book information (title, isbn (old) and isbn13 (new))
                book = Book(xml_current_book.getElementsByTagName('title')[0].firstChild.nodeValue)

                # ISBN
                old_isbn = xml_current_book.getElementsByTagName('isbn')
                if (not old_isbn[0].hasAttribute('nil')):
                    book.add_identifier({"type": "isbn", "value": old_isbn[0].firstChild.nodeValue})

                # ISBN13
                new_isbn = xml_current_book.getElementsByTagName('isbn13')
                if (not new_isbn[0].hasAttribute('nil')):
                    book.add_identifier({"type": "isbn13", "value": new_isbn[0].firstChild.nodeValue})

                # ASIN
                asin = xml_current_book.getElementsByTagName('asin')
                if (asin and (not asin[0].hasAttribute('nil'))):
                    book.add_identifier({"type": "asin", "value": asin[0].firstChild.nodeValue})

                # Authors
                authors = xml_current_book.getElementsByTagName('author')
                for author in authors:
                    book.add_author(author.getElementsByTagName('name')[0].firstChild.nodeValue)

                # Publication Year
                pub_year = xml_current_book.getElementsByTagName('publication_year')
                if (pub_year and (not pub_year[0].hasAttribute('nil'))):
                    book.publication_year(pub_year[0].firstChild.nodeValue)

                # Publisher
                publisher = xml_current_book.getElementsByTagName('publisher')
                if (publisher and (not publisher[0].hasAttribute('nil'))):
                    book.publisher(publisher[0].firstChild.nodeValue)

                isbn_list.append(book)

        # Returning the isbn list
        return isbn_list

    def get_statistics(self):
        xml = parseString(requests.get("https://www.goodreads.com/review/list", data = self.api_options).content)
        total_books = int(xml.getElementsByTagName('reviews')[0].getAttribute('total'))
        total_pages = int(total_books / self.api_options['per_page'])

        return {
            'total_books': total_books,
            'total_pages': total_pages if (total_pages > 1) else 1
        }