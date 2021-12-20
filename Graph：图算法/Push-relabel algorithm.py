# push-relabel algorithm

def MaxFlow(C, s, t):
    n = len(C)  # C is the capacity matrix
    F = [[0] * n for i in range(n)]

    # the residual capacity from u to v is C[u][v] - F[u][v]
    height = [0] * n  # height of node
    excess = [0] * n  # flow into node minus flow from node
    seen = [0] * n  # neighbours seen since last relabel

    # node list other than s and t
    nodelist = [i for i in range(n) if i != s and i != t]

    def push(u, v):
        send = min(excess[u], C[u][v] - F[u][v])
        F[u][v] += send
        F[v][u] -= send
        excess[u] -= send
        excess[v] += send

    def relabel(u):
        '''
        find smallest new height from neighbor for making a push possible
        '''
        min_height = float('inf')
        for v in range(n):
            if C[u][v] - F[u][v] > 0 and v != u:
                min_height = min(min_height, height[v])
                height[u] = min_height + 1

    def discharge(u):
        '''
        An overflowing vertex u is discharged by pushing all of its excess flow through
        admissible edges to neighboring vertices. Perform relabel if neccesary.
        '''
        while excess[u] > 0:
            if seen[u] < n:  # check next neighbour
                v = seen[u]
                #if admissive and height greater than nerghbor
                if C[u][v] - F[u][v] > 0 and height[u] > height[v]:
                    push(u, v)
                else:
                    seen[u] += 1
            else:  # we have checked all neighbours. must relabel
                relabel(u)
                seen[u] = 0

    height[s] = n  # longest path from source to sink is less than n long
    excess[s] = float("inf")
    # initialize: send as much flow as possible to neighbours of source
    for v in range(1,n):
         push(s, v)

    p = 0
    while p < len(nodelist):
        u = nodelist[p]
        old_height = height[u]
        discharge(u)
        if height[u] > old_height:
            nodelist.insert(0, nodelist.pop(p))  # move to front of list
            p = 0  # start from front of list
        else:
            p += 1
    return sum(F[s])


# C = [[0, 3, 3, 0, 0, 0],
#      [0, 0, 2, 3, 0, 0],
#      [0, 0, 0, 0, 2, 0],
#      [0, 0, 0, 0, 4, 2],
#      [0, 0, 0, 0, 0, 2],
#      [0, 0, 0, 0, 0, 3]]

#Example given in CLRS p752
C = [[0,0,14,0],
     [0,0,5,0],
     [0,0,0,8],
     [0,0,0,0]]

source = 0  # source
sink = 3  # sink

max_flow_value = MaxFlow(C, source, sink)
print("Push-Relabeled(Preflow-push) algorithm")
print("max_flow_value is: ", max_flow_value)