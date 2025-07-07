n = int(input())
    
## DFS
visited_dfs = [False] * (n + 1)

print(visited_dfs)

visited_dfs[0] = True
result_dfs = []

def dfs(v):
    if len(result_dfs) == 4:
        #print(result_dfs)
        return 0
    for i in range(1, n + 1):
        if visited_dfs[i] == False:
            visited_dfs[i] = True
            result_dfs.append(i)
            
            dfs(i)
            
            visited_dfs[i] = False
            result_dfs.pop()
            

dfs(1)