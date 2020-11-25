adj_list = {            #directed graph
    "A" : ["B", "C"],
    "B" : ["D", "E"],
    "C" : ["B", "F"],
    "D" : [],
    "E" : ["F"],
    "F" : []
}

# adj_list = { #undirected graph
#     "A" : ["B"],
#     "B" : ["D", "E"],
#     "C" : ["F"],
#     "D" : ["B"],
#     "E" : ["B"],
#     "F" : ["C"]
# }


color = {} #W, G, B
parent = {}
traversal_time = {} ##[start, end]
dfs_traversal_output = []

for node in adj_list.keys(): # for an undirecred graph, traversal starts at every node
    color[node] = "W"
    parent[node] = None
    traversal_time[node] = [-1, -1]


print(color)
print(parent)
print(traversal_time)

time = 0

def dfs_util(start_node):
    global time
    color[start_node] = "G"
    traversal_time[start_node][0] = time
    dfs_traversal_output.append(start_node)
    time += 1

    for vertice in adj_list[start_node]:
        if color[vertice] == "W":
            parent[vertice] = start_node
            dfs_util(vertice)
    color[start_node] = "B"
    traversal_time[start_node][1] = time
    time += 1

for node in adj_list.keys():
    if color[node] == "W":
        dfs_util(node)

print(dfs_traversal_output)
print(parent)
print(traversal_time)
