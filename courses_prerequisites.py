course = {
    'CSC300' : ['CSC100', 'CSC105', 'CSC200'],
    'CSC200' : ['CSC100', 'CSC105'],
    'CSC105' : [],
    'CSC100' : []
}

order_ = []

color = {} #W - white, G - grey, B - black
parent = {}
dfs_traversal_output = []

for node in course.keys(): 
    color[node] = "W"
    parent[node] = None

def dfs_util(start_node):
    color[start_node] = "G"
    # dfs_traversal_output.append(start_node)

    for vertice in course[start_node]:
        if color[vertice] == "W":
            parent[vertice] = start_node
            order_.append(vertice)
            dfs_util(vertice)
    color[start_node] = "B"

for node in course.keys(): # for an undirecred graph, traversal starts at every node
    if color[node] == "W":
        dfs_util(node)
    if node not in order_: # checks for any node not in the order_list, usually the root not CSC300
        order_.append(node)

print(order_)