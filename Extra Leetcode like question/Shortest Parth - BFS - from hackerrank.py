def bfs(n, m, edges, s):
    queue = [s]
    visited = [s]
    dists = {s: 0}
    adjList = {}
    for i in range(len(edges)):
        edge = edges[i]
        x = edge[0]
        y = edge[1]
        if x in adjList:
            if y not in adjList[x]:
                adjList[x].append(y)
        else:
            adjList[x] = [y]
        if y in adjList:
            if x not in adjList[y]:
                adjList[y].append(x)
        else:
            adjList[y] = [x]
    while len(queue) > 0:
        node = queue.pop(0)
        if node in adjList:
            neighbors = adjList[node]
            for j in range(len(neighbors)):
                if neighbors[j] not in visited:
                    dists[neighbors[j]] = dists[node] + 6
                    visited.append(neighbors[j])
                    queue.append(neighbors[j])
    res = []
    for i in range(1,n+1):
        if i not in dists:
            res.append(-1)
        elif dists[i] != 0:
            res.append(dists[i])
    return res

if __name__ == '__main__':
    n = 5 #number of nodes
    m = 3 #number of edges
    edges = [[1,2],[1,3],[3,4]]
    s = 1 #start point
    print(bfs(n, m, edges, s))