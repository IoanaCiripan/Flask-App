from bson.objectid import ObjectId
from .database import *

class Collection():
	def __init__(self, index):
		self.index = index
		self.table = database[index]
		self.new_element_added = False

	def add(self, name, description):
		element = self.format_element(name, description)
		result = database[self.index].insert_one(element)
		return result.inserted_id

	def delete_by_id(self, id):
		result = database[self.index].delete_one({"_id": ObjectId(id)})

		return 1 == result.deleted_count

	def format_element(self, name, description):
		element = {
			"name": name,
			"description": description
		}
		return element

	def get_list(self):
		result = database[self.index].find()
		return result

	def get_by_id(self, id):
		result = database[self.index].find_one({"_id": ObjectId(id)})
		return result

	def update(self, id, name, description):
		result = database[self.index].update_one(
			{ "_id": ObjectId(id)},
			{ "$set": self.format_element(name, description)}
		)
		return 1 == result.modified_count