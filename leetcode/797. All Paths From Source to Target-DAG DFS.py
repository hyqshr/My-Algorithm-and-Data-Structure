class Solution:
    def allPathsSourceTarget(self, graph):
        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    print('dfs:{}, path + [{}],path:{}'.format(i,i,path))

                    dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res
graph = [[4,3,1],[3,2,4],[3],[4],[]]
Solution().allPathsSourceTarget(graph)