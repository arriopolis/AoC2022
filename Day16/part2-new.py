import sys
import itertools as it

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

dists = {v : {w : float('inf') for w in graph} for v in graph}
for v in graph:
    dists[v][v] = 0
for v in graph:
    for (w,d) in graph[v][1]:
        dists[v][w] = d
for u in graph:
    for v in graph:
        for w in graph:
            if dists[v][w] > dists[v][u] + dists[u][w]:
                dists[v][w] = dists[v][u] + dists[u][w]

TIMELIMIT = 26
def solve(graph, dists):
    best_score = 0
    dp = {('AA', tuple()) : {0 : 0}}

    for t in range(TIMELIMIT):
        for (loc, opened), time_scores in dp.copy().items():
            if t not in time_scores: continue
            score = time_scores[t]
            flow = sum(graph[v] for v in opened)

            # Update the global best score
            projected_score = score + flow * (TIMELIMIT - t)
            best_score = max(best_score, projected_score)

            # Check if there is a more optimal path to this situation
            if any(t2 < t and score2 + flow * (t - t2) >= score for t2, score2 in time_scores.items()):
                del dp[(loc,opened)][t]
                continue

            # Try moving
            for v in graph:
                if graph[v] == 0: continue
                if v in opened: continue
                dist = dists[loc][v]
                new_t = t + dist + 1
                if new_t >= TIMELIMIT: continue

                new_opened = tuple(sorted(list(opened) + [v]))
                if (v, new_opened) not in dp: dp[(v, new_opened)] = {}
                if new_t not in dp[(v, new_opened)]: dp[(v, new_opened)][new_t] = 0
                dp[(v, new_opened)][new_t] = max(dp[(v, new_opened)][new_t], score + flow * (dist + 1))

    return best_score

overall_best_score = 0
nodes = set(graph.keys())
nodes.remove('AA')
n = len(nodes)//2
for r in range(n+1):
    print(r, '/', n, '           ')
    ss = list(it.combinations(nodes, r))
    for j,s in enumerate(ss):
        print(j, '/', len(ss), end = '\r')
        s = set(s).union(['AA'])
        nots = nodes.difference(s).union(['AA'])

        # Make your graph and distance table
        your_graph = {v : rate for v,(rate,_) in graph.items() if v in s}
        your_dists = {v : {w : d for w,d in x.items() if w in s} for v,x in dists.items() if v in s}
        your_score = solve(your_graph, your_dists)

        # Make the elephant's graph
        el_graph = {v : rate for v,(rate,_) in graph.items() if v in nots}
        el_dists = {v : {w : d for w,d in x.items() if w in nots} for v,x in dists.items() if v in nots}
        el_score = solve(el_graph, el_dists)

        overall_best_score = max(overall_best_score, your_score + el_score)

print()
print(overall_best_score)
