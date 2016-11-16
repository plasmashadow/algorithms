from collections import Iterable

class Traversor(Iterable):

	def __init__(self, root):
		self.root = root

	def __iter__(self):
		raise NotImplemented

class InorderTraversor(Traversor):

	def __init__(self, *args, **kwargs):
		super(InorderTraversor, self).__init__(*args, **kwargs)

	def __iter__(self):
		for l in iter(self.root.left): yield l
		yield self.root
		for r in iter(self.root.right):yield r

class PreOrderTraversor(Traversor):

	def __init__(self, *args, **kwargs):
		super(PreOrderTraversor, self).__init__(*args, **kwargs)

	def __iter__(self):
		yield self.root
		for l in iter(self.root.left): yield l
		for r in iter(self.root.right):yield r

class PostOrderTraversor(Traversor):

	def __init__(self, *args, **kwargs):
		super(PostOrderTraversor, self).__init__(*args, **kwargs)

	def __iter__(self):
		for l in iter(self.root.left): yield l
		for r in iter(self.root.right):yield r
		yield self.root

