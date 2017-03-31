class Book(object):

    def __init__(self, title):
    	self._title = title
    	self._authors = []
    	self._identifier = []
    	self._publication_year = 0
    	self._publisher = "None"

    def add_identifier(self, id):
    	self._identifier.append(id)

    def add_author(self, author):
    	self._authors.append(author)

    '''
	
			Getters and Setters

	'''
    @property
    def title(self):
    	return self._title

    @property
    def authors(self):
    	return self._authors

    @property
    def identifier(self):
    	return self._identifier

    @property
    def publisher(self):
    	return self._publisher

    @property
    def publication_year(self):
    	return self._publication_year

    @publication_year.setter
    def publication_year(self, year):
    	self._publication_year = year

    @publisher.setter
    def publisher(self, pub):
    	self._publisher = pub

    @title.setter
    def title(self, title):
    	self._title = title

    @authors.setter
    def authors(self, authors):
    	self._authors = authors

    @identifier.setter
    def identifier(self, identifier):
    	self._identifier = identifier


