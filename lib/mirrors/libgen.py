import requests
from xml.dom.minidom import parseString
from htmldom import htmldom
import libgenapi
import time
import json

class Libgen(object):

    def __init__(self, isbn_list, mirrors = ["http://libgen.io/", "http://gen.lib.rus.ec/", "http://libgen.net/", "http://bookfi.org/"]):
        self.mirrors = mirrors
        self.lg = libgenapi.Libgenapi(mirrors)
        self.isbn_list = isbn_list

    def find_single(self, book):
        '''
            Tries to find a single book in the database based on it's ISBN or ISBN13.
        '''
        download_url = None

        # Trying to download via ISBN or via ISBN13
        if ('isbn' in book): download_url = self.inner_find(book['isbn'])
        if ('isbn13' in book): download_url = self.inner_find(book['isbn13'])

        if (download_url):
            print("[FOUND] Book {} found.".format(book['title']))
        else:
            print("[ERROR] Book {} not found.".format(book['title']))

        return download_url

    def find(self):
        total = len(self.isbn_list)
        download_urls = [] # Success

        for book in self.isbn_list:
            time.sleep(1)
            current = self.find_single(book)
            if (current): download_urls.append(current)

        print("=== Summary ===")
        print("Success: {}".format(str(len(download_urls))))
        print("Total: {}".format(str(total)))
        return download_urls

    def download_single(self, book, find=True):
        download_url = self.find_single(book) if (find) else book
        if (download_url): self.inner_download(url=download_url[0], filename=("downloads/" + book['title'] + "." + download_url[1]))

    def download(self):
        download_urls = self.find()
        for download in download_urls:
            time.sleep(1)
            self.download_single(download, find=False)


    # Private methods
    def inner_find(self, isbn):
        results = self.lg.search(isbn, "identifier")
        for result in results:
            if ((result['extension'] == 'epub') or (result['extension'] == 'mobi')):
                mirror = result['mirrors'][0]
                dom = htmldom.HtmlDom("http://libgen.io" + mirror).createDom()
                # dom = htmldom.HtmlDom(mirror).createDom()
                h2s = dom.find('h2')
                for h2 in h2s:
                    if (h2.text().lower() == "download"):
                        return [h2.parent().attr('href'), result['extension']]
        return None

    def inner_download(self, url, filename):
        with open(filename, "wb") as handle:
            response = requests.get("http://libgen.io" + url, stream=True)
            if not response.ok: return False

            print("Downloading book to {}".format(filename))

            for block in response.iter_content(1024):
                handle.write(block)
        return True
