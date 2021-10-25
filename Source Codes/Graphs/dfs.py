class Solution:
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self,i,vis,q,adj):
        vis[i]=1
        q.append(i)
        for i in adj[i]:
            if(vis[i]==0):
                self.dfs(i,vis,q,adj)
    
    def dfsOfGraph(self, V, adj):
        vis=[0 for i in range(V)]
        q=[]
        self.dfs(0,vis,q,adj)
        return q
        # code here
#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        V, E = map(int, input().split())
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
# } Driver Code Ends