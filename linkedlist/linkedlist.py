class ListNode:
	def __init__(self, data): 
		# store data
		self.data = data
		#store the reference (next item)
		self.next = None  
	def copy(self):
		x=ListNode(self.data)
		x.next=self.next
		return x

class SingleLinkedList:
	def __init__(self): 
		self.root = None
		return
	def add_list_item(self, item):
		if not isinstance(item, ListNode):
			item = ListNode(item)
		if self.root is None:
			self.root=item
		else:
			item.next=self.root
			self.root=item
		return

	def delete(self, value):
		curr=self.root
		previous=None
		while curr is not None:
			if curr.data==value:
				if previous:
					previous.next=curr.next
				else:
					self.root=curr.next
				return True
			else:
				previous=curr
				curr=curr.next
		return False
	def printall(self):
		curr=self.root
		tmp=""
		while curr is not None:
			tmp=tmp+str(curr.data)+'->'
			curr=curr.next
		print(tmp[:-2])