class Solution:
    def dfs(self, node, adj, vis, ls):
        vis[node] = 1
        ls.append(node)

        # traverse all its neighbours
        for it in adj[node]:
            if not vis[it]:
                self.dfs(it, adj, vis, ls)

    # Function to return a list containing the DFS traversal of the graph
    def dfsOfGraph(self, V, adj):
        vis = [0] * V
        start = 0
        ls = []
        self.dfs(start, adj, vis, ls)
        return ls


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)  # undirected graph


def printAns(ans):
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    V = 5
    adj = [[] for _ in range(V)]

    addEdge(adj, 0, 2)
    addEdge(adj, 2, 4)
    addEdge(adj, 0, 1)
    addEdge(adj, 0, 3)

    obj = Solution()
    ans = obj.dfsOfGraph(V, adj)
    printAns(ans)
