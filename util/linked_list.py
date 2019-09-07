class LinkedList:
	def __init__(self):
		self.size = 0
		self.head = self.tail = None

	@staticmethod
	def initFromList(list):
		ll = LinkedList()

		for item in list:
			ll.addBack(item)

		return ll

	def addFront(item):
		if(self.head is None and self.tail is None):
			initLinkedList(item)
			return

		self.head.prevNode = Node(None, self.head, item)
		self.head = self.head.prevNode	
		self.size += 1

	def addBack(item):
		if(self.head is None and self.tail is None):
			initLinkedList(item)
			return

		self.tail.next = Node(self.tail, None, item)
		self.tail = self.tail.next
		self.size += 1

	def initLinkedList(item):
		self.head = self.tail = Node(None, None, item)
		self.size += 1;

class Node:
	def __init__(self, prevNode, nextNode, item):
		self.prevNode = prevNode
		self.nextNode = nextNode
		self.item = item
