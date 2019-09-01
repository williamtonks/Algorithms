import Queue
import networkx as nx
from networkx.algorithms import bipartite
#Failing because our tiling is disconnected.
with open('art.txt') as f:
    firstLine = f.readline()
    firsty = firstLine.split()
    numNodes = 0;
    cols = int(firsty[0])
    rows = int(firsty[1])
    theArt = [["0" for y in range(cols)] for x in range(rows)]
    data = f.readlines()
    x = 0
    for line in data:
        y = 0
        while y < cols:
            theArt[x][y] = line[y]
            y+=1
        x+=1
    start = "B"
    forget = True
    for x in range(rows):
        for y in range(cols):
                if theArt[x][y] == "#" and forget:
                    forget = False
                    start+=str(x)
                    start+=str(y)
                    numNodes +=1
                    theArt[x][y] = start
                elif theArt[x][y] == "#" and not forget:
                    theArt[x][y] = str(x) + str(y)
                    numNodes+=1
    nodestoVisit = numNodes;
    while nodestoVisit > 0:
        toVisit = Queue.Queue(maxsize = 0)
        toVisit.put(start)
        while toVisit.qsize() > 0:
            currentNode = toVisit.get()
            nodestoVisit -=1
            if int(currentNode[1])-1 >=0 :
                if not theArt[int(currentNode[1])-1][int(currentNode[2])] == "." and not theArt[int(currentNode[1])-1][int(currentNode[2])][0] == "B" and not theArt[int(currentNode[1])-1][int(currentNode[2])][0] == "R" :
                    if currentNode[0] == "B":
                        theArt[int(currentNode[1])-1][int(currentNode[2])] = "R" + theArt[int(currentNode[1])-1][int(currentNode[2])]
                        toVisit.put(theArt[int(currentNode[1])-1][int(currentNode[2])])
                    else :
                        theArt[int(currentNode[1])-1][int(currentNode[2])] = "B" + theArt[int(currentNode[1])-1][int(currentNode[2])]
                        toVisit.put(theArt[int(currentNode[1])-1][int(currentNode[2])])
            if int(currentNode[1])+1 <= rows-1 :
                if not theArt[int(currentNode[1])+1][int(currentNode[2])] == "." and not theArt[int(currentNode[1])+1][int(currentNode[2])][0] == "B" and not theArt[int(currentNode[1])+1][int(currentNode[2])][0] == "R" :
                    if currentNode[0] == "B":
                        theArt[int(currentNode[1])+1][int(currentNode[2])] = "R" + theArt[int(currentNode[1])+1][int(currentNode[2])]
                        toVisit.put(theArt[int(currentNode[1])+1][int(currentNode[2])] )
                    else :
                        theArt[int(currentNode[1])+1][int(currentNode[2])] = "B" + theArt[int(currentNode[1])+1][int(currentNode[2])]
                        toVisit.put(theArt[int(currentNode[1])+1][int(currentNode[2])])
            if int(currentNode[2])-1 >= 0 :
                if not theArt[int(currentNode[1])][int(currentNode[2])-1] == "." and not theArt[int(currentNode[1])][int(currentNode[2])-1][0] == "B" and not theArt[int(currentNode[1])][int(currentNode[2])-1][0] == "R":
                    if currentNode[0] == "B":
                        theArt[int(currentNode[1])][int(currentNode[2])-1] =  "R" + theArt[int(currentNode[1])][int(currentNode[2])-1]
                        toVisit.put(theArt[int(currentNode[1])][int(currentNode[2])-1])
                    else :
                        theArt[int(currentNode[1])][int(currentNode[2])-1] = "B" + theArt[int(currentNode[1])][int(currentNode[2])-1]
                        toVisit.put(theArt[int(currentNode[1])][int(currentNode[2])-1])
            if int(currentNode[2])+1 <= cols-1 :
                if not theArt[int(currentNode[1])][int(currentNode[2])+1] == "." and not theArt[int(currentNode[1])][int(currentNode[2])+1][0] == "B" and not theArt[int(currentNode[1])][int(currentNode[2])+1][0] == "R":
                    if currentNode[0] == "B":
                        theArt[int(currentNode[1])][int(currentNode[2])+1] =  "R" + theArt[int(currentNode[1])][int(currentNode[2])+1]
                        toVisit.put(theArt[int(currentNode[1])][int(currentNode[2])+1])
                    else :
                        theArt[int(currentNode[1])][int(currentNode[2])+1] =  "B" + theArt[int(currentNode[1])][int(currentNode[2])+1]
                        toVisit.put(theArt[int(currentNode[1])][int(currentNode[2])+1])
        if(nodestoVisit > 0):
            forget = True
            for x in range(rows):
                for y in range(cols):
                    if not theArt[x][y] == "." and not theArt[x][y][0] == "B" and not theArt[x][y][0] == "R" and forget:
                        forget = False
                        start = "B"
                        start+=str(x)
                        start+=str(y)
                        theArt[x][y] = start
    blueNodes = []
    redNodes = []
    for x in range(rows):
        for y in range(cols):
            if theArt[x][y][0] == "B":
                blueNodes.append(theArt[x][y])
            elif theArt[x][y][0] == "R":
                redNodes.append(theArt[x][y])
    edges = []
    for x in range(rows):
        for y in range(cols):
            if theArt[x][y][0] == "B" :
                if x-1 >= 0 :
                    if theArt[x-1][y][0] == "R":
                        blue = theArt[x][y]
                        red = theArt[x-1][y]
                        edges.append([blue, red])
                if x+1 <= rows-1 :
                    if theArt[x+1][y][0] == "R":
                        blue = theArt[x][y]
                        red = theArt[x+1][y]
                        edges.append([blue, red])
                if y-1 >= 0 :
                    if theArt[x][y-1][0] == "R":
                        blue = theArt[x][y]
                        red = theArt[x][y-1]
                        edges.append([blue, red])
                if y+1 <= cols-1 :
                    if theArt[x][y+1][0] == "R":
                        blue = theArt[x][y]
                        red = theArt[x][y+1]
                        edges.append([blue, red])
    B = nx.Graph()
    B.add_nodes_from(blueNodes, bipartite=0) # Add the node attribute "bipartite"
    B.add_nodes_from(redNodes, bipartite=1)
    B.add_edges_from(edges, capacity = 1)
    final = nx.bipartite.maximum_matching(B)
    finalPrintyBoi = []
    if(len(final) == numNodes):
        for x in blueNodes:
            blueGuy = x
            redGuy = final[blueGuy]
            finalPrintyBoi.append(blueGuy[2] +" " + blueGuy[1]+ " " + redGuy[2]+" "+redGuy[1])
        for y in finalPrintyBoi:
            print(y)
    else:
        print("Impossible")

def FordFulkerson(blueNodes, redNodes, edges):

        max_flow = 0 # There is no flow initially
        source = source
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent) :

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while(s !=  source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow +=  path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while(v !=  source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow
