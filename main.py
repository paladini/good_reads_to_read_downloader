#!/usr/bin/python3

from lib.input.goodreads import GoodReads
from lib.mirrors.libgen import Libgen

# Importing books from GoodReads
gr = GoodReads(key='ZEZz677VsuEPhwZoc0hrw', user_id='51988336')
isbn_list = gr.get_books(to_page=1)

# print(isbn_list)

for book in isbn_list:
	print(book.title)
	print(book.identifier)
	print(book.authors)
	print(book.publisher)
	print(book.publication_year)
	print("\n\n")

# Downloading books from Libgen
# libgen = Libgen(isbn_list)
# libgen.download_single(isbn_list[0])