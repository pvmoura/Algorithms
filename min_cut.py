import copy
import random

def karger_algo(graph):
	while len(graph['nodes']) > 2:
		edge = graph['edges'][random.randint(0, len(graph['edges']) - 1)]
		graph = collapse_edge(edge, graph)
	for val in graph['nodes'].itervalues():
		return len(val)

def collapse_edge(edge, graph):
	first_node = edge[0]
	second_node = edge[1]
	for index in graph['nodes'][second_node]:
		if first_node in graph['edges'][index]:
			graph['nodes'][first_node].remove(index)
			graph = update_edge_indices(graph, index)
			del graph['edges'][index]
		else:
			tup_index = graph['edges'][index].index(second_node)
			graph['edges'][index] = (graph['edges'][index][tup_index - 1], first_node)
			graph['nodes'][first_node].append(index)
	del graph['nodes'][second_node]
	return graph

def update_edge_indices(graph, deleted_index):
	for key, val in graph['nodes'].iteritems():
		for index, elem in enumerate(val):
			if elem > deleted_index:
				val[index] -= 1
	return graph

if __name__ == "__main__":
	graph = {
		'nodes': {},
		'edges': []
	}
	if False:
		f = open('test2.txt', 'r')
	else:
		f = open('kargerMinCut.txt', 'r')

	lines = f.readlines()
	for i in range(1, len(lines) + 1):
		graph['nodes'][i] = []

	for line in lines:
		temp = line.rstrip().split('\t')
		start = int(temp.pop(0))
		for elem in temp:
			tup = ((start, int(elem)))
			if tup not in graph['edges'] and \
			(tup[1], tup[0]) not in graph['edges']:
				edge_index = len(graph['edges'])
				graph['nodes'][start].append(edge_index)
				graph['nodes'][tup[1]].append(edge_index)
				graph['edges'].append(tup)
	f.close()
	min_cut = len(graph['edges'])
	for i in range(500):
		new_graph = copy.deepcopy(graph)
		potential_min_cut = karger_algo(new_graph)
		if potential_min_cut < min_cut:
			min_cut = potential_min_cut
	print 'the min-cut is:', min_cut