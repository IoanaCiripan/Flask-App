from bson.objectid import ObjectId
from .database import *

class Collection():
	def __init__(self, index):
		self.index = index
		self.table = database[index]
		self.new_element_added = False

	def add(self, **dictionary):
		element = self.format_element(**dictionary)
		result = database[self.index].insert_one(element)
		self.new_element_added = True
		return result.inserted_id

	def delete_by_id(self, id):
		result = database[self.index].delete_one({"_id": ObjectId(id)})

		return 1 == result.deleted_count

	def get_first(self):
		result = database[self.index].find_one()
		return result

	def get_list(self):
		result = database[self.index].find()
		return result

	def get_by_id(self, id):
		result = database[self.index].find_one({"_id": ObjectId(id)})
		return result

	def format_element (self, **dictionary):
		return dictionary

	def update(self, id, **dictionary):
		element = self.format_element(**dictionary)
		result = database[self.index].update_one(
			{ "_id": ObjectId(id)},
			{ "$set": self.format_element(element)}
		)
		return 1 == result.modified_count