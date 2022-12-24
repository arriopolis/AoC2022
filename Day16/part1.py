import sys

graph = {}
for line in sys.stdin:
    valve, tunnels = line.strip().split('; ')
    valve = valve.split()
    rate = int(valve[-1].split('=')[1])
    name = valve[1]
    tunnels = list(map(lambda x : x.rstrip(','), tunnels.split()[4:]))
    graph[name] = (rate,tunnels)

graph = {name : (rate, set([(t,1) for t in tunnels])) for name,(rate,tunnels) in graph.items()}
while any(len(tunnels) == 2 and rate == 0 for name,(rate,tunnels) in graph.items()):
    name = next(name for name,(rate,tunnels) in graph.items() if len(tunnels) == 2 and rate == 0)
    _,((v,dv),(w,dw)) = graph[name]
    graph[v][1].remove((name,dv))
    graph[v][1].add((w,dv+dw))
    graph[w][1].remove((name,dw))
    graph[w][1].add((v,dv+dw))
    del graph[name]

best_score = 0
TIMELIMIT = 30

dp = {}

def DFS(loc, t, score = 0, opened = set(), visited = set()):
    global best_score, dp

    if t >= TIMELIMIT: return
    if loc in visited: return
    flow = sum(graph[v][0] for v in opened)
    total_score = score + flow * (TIMELIMIT - t)
    best_score = max(best_score, total_score)

    key = (loc, tuple(sorted(opened)))
    if key in dp:
        for prev_score, prev_t in dp[key]:
            if prev_score >= total_score and prev_t <= t: return
    else:
        dp[key] = set()
    dp[key].add((total_score, t))

    if loc not in opened and graph[loc][0] > 0:
        DFS(loc, t+1, score = score + flow, opened = opened.union([loc]), visited = set())

    for v,dist in graph[loc][1]:
        DFS(v, t+dist, score = score + flow * dist, opened = opened.copy(), visited = visited.union([loc]))

DFS('AA', 0)
print(best_score)
