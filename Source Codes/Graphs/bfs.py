class Solution:   
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        q=[0]
        vis=[0 for i in range(V)]
        vis[0]=1
        res=[0]
        while(q):
            t=q.pop(0)
            for i in adj[t]:
                if(vis[i]==0):
                    q.append(i)
                    res.append(i)
                    vis[i]=1
        return res
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
        ob = Solution()
        ans = ob.bfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
# } Driver Code Ends