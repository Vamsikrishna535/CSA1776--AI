# Python3 program for the above approach

# Number of vertices in the graph
# define 4 4

# check if the colored
# graph is safe or not


def isSafe(graph, color):

	# check for every edge
	for i in range(4):
		for j in range(i + 1, 4):
			if (graph[i][j] and color[j] == color[i]):
				return False
	return True

# /* This function solves the m Coloring
# problem using recursion. It returns
# false if the m colours cannot be assigned,
# otherwise, return true and prints
# assignments of colours to all vertices.
# Please note that there may be more than
# one solutions, this function prints one
# of the feasible solutions.*/


def graphColoring(graph, m, i, color):

	# if current index reached end
	if (i == 4):

		# if coloring is safe
		if (isSafe(graph, color)):

			# Print the solution
			printSolution(color)
			return True
		return False

	# Assign each color from 1 to m
	for j in range(1, m + 1):
		color[i] = j

		# Recur of the rest vertices
		if (graphColoring(graph, m, i + 1, color)):
			return True
		color[i] = 0
	return False

G = [[ 0, 1, 1, 0, 1, 0],
     [ 1, 0, 1, 1, 0, 1],
     [ 1, 1, 0, 1, 1, 0],
     [ 0, 1, 1, 0, 0, 1],
     [ 1, 0, 1, 0, 0, 1],
     [ 0, 1, 0, 1, 1, 0]]



# inisiate the name of node.
node = "abcdef"
t_={}
for i in range(len(G)):
  t_[node[i]] = i

# count degree of all node.
degree =[]
for i in range(len(G)):
  degree.append(sum(G[i]))

# inisiate the posible color
colorDict = {}
for i in range(len(G)):
  colorDict[node[i]]=["Blue","Red","Yellow","Green"]


# sort the node depends on the degree
sortedNode=[]
indeks = []

# use selection sort
for i in range(len(degree)):
  _max = 0
  j = 0
  for j in range(len(degree)):
    if j not in indeks:
      if degree[j] > _max:
        _max = degree[j]
        idx = j
  indeks.append(idx)
  sortedNode.append(node[idx])

# The main process
theSolution={}
for n in sortedNode:
  setTheColor = colorDict[n]
  theSolution[n] = setTheColor[0]
  adjacentNode = G[t_[n]]
  for j in range(len(adjacentNode)):
    if adjacentNode[j]==1 and (setTheColor[0] in colorDict[node[j]]):
      colorDict[node[j]].remove(setTheColor[0])


# Print the solution
for t,w in sorted(theSolution.items()):
  print("Node",t," = ",w)
