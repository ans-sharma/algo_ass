
INF = 9999999
noOfNodes = 4
graph = [[0, 4, 0, 5],
     [4, 0, 1, 0],
     [0, 1, 0, 2],
     [5, 0, 2, 0]]

selectedNodeFlag = [0, 0, 0, 0]
temp = 0
selectedNodeFlag[0] = True
print("Selected Nodes with their cost: ")
while (temp < noOfNodes - 1):
    
    minimum = INF
    a = 0
    b = 0
    for x in range(noOfNodes):
        if selectedNodeFlag[x]:
            for y in range(noOfNodes):
                if ((not selectedNodeFlag[y]) and graph[x][y]):  
                    if minimum > graph[x][y]:
                        minimum = graph[x][y]
                        a = x
                        b = y
    print(str(a) + " - " + str(b) + ": " + str(graph[a][b]))
    selectedNodeFlag[b] = True
    temp += 1