class Heap():
	def __init__(self, heap_type='min', *args):
		self.heap_type = heap_type
		self.heap_array = [arg for arg in args if self.type_check(arg)]
		for index, arg in enumerate(reversed(self.heap_array)):
			self.bubble_up(index)

	def __repr__(self, ):
		return str(self.heap_array)

	def type_check(self, input):
		if type(input) is not tuple:
			raise ValueError('Heap only allows key, value pairs as tuples: (key, value)')
		elif len(input) != 2:
			raise ValueError('Heap only allows key, value pairs as tuples: (key, value)')
		return input

	def insert(self, elem):
		self.type_check(elem)
		self.heap_array.append(elem)
		self.bubble_up(len(self.heap_array) - 1)

	def pop_root(self, ):
		ret = self.heap_array[0]
		self.heap_array[0] = self.heap_array.pop()
		self.bubble_down()
		return ret

	def get_parent_index(self, index):
		return (index - 1)/2

	def delete(self, index):
		try:
			element = self.heap_array.pop(index)
		except IndexError:
			raise IndexError('Heap index out of range')
		self.heap_array, rest = self.heap_array[:index], self.heap_array[index:]
		for elem in rest:
			self.insert(elem)

	def compare_elements(self, first_ind, second_ind):
		key1 = self.heap_array[first_ind][0]
		key2 = self.heap_array[second_ind][0]
		if key1 > key2:
			return 1
		elif key1 < key2:
			return -1
		else:
			return 0

	def swap(self, first_ind, second_ind):
		self.heap_array[first_ind], self.heap_array[second_ind] = \
		self.heap_array[second_ind], self.heap_array[first_ind]

	def bubble_up(self, index):
		par = self.get_parent_index(index)
		ext_val = -1 if self.heap_type == 'min' else 1
		while self.compare_elements(index, par) == ext_val and index != 0:
			self.swap(index, par)
			index = par
			par = self.get_parent_index(index)

	def get_child_index(self, index):
		try:
			left = 2*index+1
			ext = min if self.heap_type == 'min' else max
			children = [(left, self.heap_array[left]),
						(left + 1, self.heap_array[left + 1])]
			return ext(children, key=lambda tup: tup[1][0])[0]
		except IndexError:
			return False

	def bubble_down(self, index=0):
		c_ind = self.get_child_index(index)
		ext = min if self.heap_type == 'min' else max
		while (c_ind and
		self.heap_array[c_ind] == ext(self.heap_array[index], self.heap_array[c_ind])
		):
			self.swap(c_ind, index)
			index = c_ind
			c_ind = self.get_child_index(index)


def test_for_equality(list1, list2):
	for elem in list1:
		if elem not in list2:
			return False
	return True if len(list1) == len(list2) else False

if __name__ == "__main__":

	if True:
		f = open('dijkstra_test.txt', 'r')
	else:
		f = open('dijkstraData.txt', 'r')

	lines = f.readlines()
	f.close()
	distances = {}
	graph = {}
	seen_nodes = []
	for index, line in enumerate(lines):
		temp = line.rstrip().split('\t')
		start = int(temp.pop(0))
		graph[start] = [(int(elem.split(',')[0]), int(elem.split(',')[1]))
										 for elem in temp]
		if index == 0:
			distances[start] = 0
			i = start
			seen_nodes.append(start)
		else:
			distances[start] = 1000000

	
	while not test_for_equality(seen_nodes, graph.keys()):
		min_dist = None
		pot_node = None
		pot_start = None
		for node in seen_nodes:
			for edge in graph[node]:
				if edge[0] not in seen_nodes:
					potential_dist = distances[node] + edge[1]
					if not pot_node or potential_dist < min_dist:
						pot_start = node
						pot_node = edge[0]
						min_dist = potential_dist

		if pot_node:
			distances[pot_node] = min_dist
			seen_nodes.append(pot_node)

	if False:
		pset_answers = '7,37,59,82,99,115,133,165,188,197'
		answers = []
		for location in pset_answers.split(','):
			print location, distances[int(location)]
			answers.append(str(distances[int(location)]))
		print 'answers:', ','.join(answers)
	print distances
	
	