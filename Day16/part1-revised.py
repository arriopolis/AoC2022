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

dp = {0 : {('AA', tuple()) : 0}}
best_score = 0
for t in range(TIMELIMIT+1):
    for (loc, opened), score in dp[t].items():
        best_score = max(best_score, score)
        flow = sum(graph[v][0] for v in opened)

        # Try staying stationary
        if t+1 <= TIMELIMIT:
            key = (loc, opened)
            if t+1 not in dp: dp[t+1] = {}
            if key not in dp[t+1]: dp[t+1][key] = 0
            dp[t+1][key] = max(dp[t+1][key], score + flow)

        # Try opening
        if t+1 <= TIMELIMIT and loc not in opened:
            new_opened = tuple(sorted(list(opened) + [loc]))
            key = (loc, new_opened)
            if t+1 not in dp: dp[t+1] = {}
            if key not in dp[t+1]: dp[t+1][key] = 0
            dp[t+1][key] = max(dp[t+1][key], score + flow)

        # Try moving
        for name, dist in graph[loc][1]:
            key = (name, opened)
            if t+dist > TIMELIMIT: continue
            if t+dist not in dp: dp[t+dist] = {}
            if key not in dp[t+dist]: dp[t+dist][key] = 0
            dp[t+dist][key] = max(dp[t+dist][key], score + dist * flow)

print(best_score)
