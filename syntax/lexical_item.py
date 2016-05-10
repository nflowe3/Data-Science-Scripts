
class LexicalItem(object):

	def __init__(self, label, lexical_entry):
		self.label = label
		self.lexical_entry = lexical_entry

	def __str__(self):
		return self.lexical_entry

class MergeProduct(object):

	def __init__(self):
		self.projection = None
		self.projection_item = ""
		self.lex_item_list = []

	def merge(self, a, b):
		
		if type(a) is LexicalItem and type(b) is LexicalItem:
			self.projection = a.label
			self.projection_item = a.lexical_entry
			self.lex_item_list = [a, [a, b]]

		if type(a) is LexicalItem and type(b) is MergeProduct:
			self.projection = a.projection
			self.projection_item = a.projection_item
			self.lex_item_list = [a.projection_item, [b, a]]

	def printcontent(self, contents=self.lex_item_list):
		for lex in contents:
			if type(lex) is list:
				printcontent()
			

a = LexicalItem("V", "eat")
b = LexicalItem("N", "cake")
c = LexicalItem("D", "I")

VBar = MergeProduct()
VP = MergeProduct()

VBar.merge(a, b)
VBar.printcontent()