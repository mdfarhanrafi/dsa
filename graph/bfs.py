from collections import deque


class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        vis = [0] * V
        vis[0] = 1
        q = deque([0])   # queue for BFS
        bfs = []

        while q:
            node = q.popleft()
            bfs.append(node)

            # traverse all neighbors
            for it in adj[node]:
                if not vis[it]:
                    vis[it] = 1
                    q.append(it)

        return bfs


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)  # undirected graph


def printAns(ans):
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    V = 6
    adj = [[] for _ in range(V)]

    addEdge(adj, 0, 1)
    addEdge(adj, 1, 2)
    addEdge(adj, 1, 3)
    addEdge(adj, 0, 4)

    obj = Solution()
    ans = obj.bfsOfGraph(5, adj)  # here V=5 (nodes 0..4)
    printAns(ans)
