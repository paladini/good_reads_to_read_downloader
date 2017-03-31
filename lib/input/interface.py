from abc import ABC, abstractmethod

class Interface(ABC):

	def __init__(options):
		self.options = options

	@abstractmethod
	def get_books():
		pass