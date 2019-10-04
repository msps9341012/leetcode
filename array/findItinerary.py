from collections import deque
def build_graph(tickets):
    G = {}
    for t in tickets:
        S, E = t
        G[S] = G.get(S, []) + [E]
    for A in G:
        G[A].sort(reverse=True)
        G[A] = deque(G[A])
    return G

def dfs(G, S):
    trip.append(S)
    if len(trip) == length:
        return True
    if S in G:
        n, i = len(G[S]), 0
        while i < n:
            A = G[S].pop()
            if dfs(G, A):
                return True
            G[S].appendleft(A)
            i += 1
    print(trip)
    trip.pop()
    return False
    
tickets=[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]

G = build_graph(tickets)
print(G)
trip, length = [], len(tickets) + 1
dfs(G, "JFK")


