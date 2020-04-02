from .collection import *

collection = Collection("elements")

project = {
	"name": "Demo",
	"element": "element"
}

page = {
	"home": "Home",
	"add": "Add " + project["element"],
	"delete": "Delete " + project["element"],
	"view": "View " + project["element"]
}