def reverse_graph(graph):
  new_graph = {}
  for head in graph.iterkeys():
    for tail in graph[head]:
      if not new_graph.get(tail):
        new_graph[tail] = []
      new_graph[tail].append(head)
  return new_graph


def DFS(graph, start, explored=None, finishing_times=None,
        leader=None, leaders=None, paths=None):
  if paths is None:
    paths = []
  if explored is None:
    explored = []
  explored.append(start)
  if leader is not None:
    leaders[start] = leader

  nodes = graph.get(start)
  if nodes is not None:
    for node in nodes:
      if node not in explored:
        paths.append(node)
        DFS(graph, node, explored, finishing_times, leader, leaders, paths)
  if finishing_times is not None and start not in finishing_times:
    finishing_times.append(start)
  return paths

if __name__ == "__main__":
  #for i in range(1,6):
  graph = {}
  leaders = {}
  #with open('kosaraju_test_' + str(i) + '.txt', 'r') as f:
  with open('SCC.txt', 'r') as f:
    for line in f:
      l_list = [int(elem) for elem in line.rstrip().split(' ')]
      head = l_list.pop(0)
      if not graph.get(head):
        graph[head] = []
      graph[head].extend(l_list)

  reversed_graph = reverse_graph(graph)
  keys_list = graph.keys()
  start = max(keys_list)
  end = min(keys_list)
  paths = {}
  finishing_times = []
  explored = []
  while start >= end:
    DFS(reversed_graph, start, explored, finishing_times)
    start -= 1
  explored = []
  for index, start in enumerate(reversed(finishing_times)):
    if start not in explored:
      leader = start
      paths[start] = DFS(graph, start, explored, None, leader, leaders)

  SCC_sizes = []
  for key, val in paths.iteritems():
    SCC_sizes.append(len(val) + 1)
  SCC_sizes.sort(reverse=True)
  print SCC_sizes

