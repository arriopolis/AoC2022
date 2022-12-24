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
TIMELIMIT = 26

dp = {0 : {('AA', 'AA', 0, 0, tuple()) : 0}}
best_score = 0

for t in range(TIMELIMIT+1):
    print(t)
    for (loc1, loc2, time_left1, time_left2, opened), score in dp[t].items():
        best_score = max(best_score, score)
        flow = sum(graph[v][0] for v in opened)

        if t >= TIMELIMIT: continue

        if time_left1 > 0 and time_left2 > 0:
            # Simulate
            key = (loc1, loc2, time_left1-1, time_left2-1, opened)
            if t+1 not in dp: dp[t+1] = {}
            if key not in dp[t+1]: dp[t+1][key] = 0
            dp[t+1][key] = max(dp[t+1][key], score + flow)

        elif time_left1 == 0 and time_left2 > 0:
            # Try player1 staying stationary
            key = (loc1, loc2, 0, time_left2-1, opened)
            if t+1 not in dp: dp[t+1] = {}
            if key not in dp[t+1]: dp[t+1][key] = 0
            dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player1 opening
            if loc1 not in opened and graph[loc1][0] > 0:
                new_opened = tuple(sorted(list(opened) + [loc1]))
                key = (loc1, loc2, 0, time_left2-1, new_opened)
                if t+1 not in dp: dp[t+1] = {}
                if key not in dp[t+1]: dp[t+1][key] = 0
                dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player1 moving
            for name, dist in graph[loc1][1]:
                if t+dist > TIMELIMIT: continue
                key = (name, loc2, dist-1, time_left2-1, opened)
                if t+1 not in dp: dp[t+1] = {}
                if key not in dp[t+1]: dp[t+1][key] = 0
                dp[t+1][key] = max(dp[t+1][key], score + flow)

        elif time_left1 > 0 and time_left2 == 0:
            # Try player2 staying stationary
            key = (loc1, loc2, time_left1-1, 0, opened)
            if t+1 not in dp: dp[t+1] = {}
            if key not in dp[t+1]: dp[t+1][key] = 0
            dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player2 opening
            if loc2 not in opened and graph[loc2][0] > 0:
                new_opened = tuple(sorted(list(opened) + [loc2]))
                key = (loc1, loc2, time_left1-1, 0, new_opened)
                if t+1 not in dp: dp[t+1] = {}
                if key not in dp[t+1]: dp[t+1][key] = 0
                dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player2 moving
            for name, dist in graph[loc2][1]:
                if t+dist > TIMELIMIT: continue
                key = (loc1, name, time_left1-1, dist-1, opened)
                if t+1 not in dp: dp[t+1] = {}
                if key not in dp[t+1]: dp[t+1][key] = 0
                dp[t+1][key] = max(dp[t+1][key], score + flow)

        else:
            # Try player1 and player2 staying stationary
            key = (loc1, loc2, 0, 0, opened)
            if t+1 not in dp: dp[t+1] = {}
            if key not in dp[t+1]: dp[t+1][key] = 0
            dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player1 staying stationary and player2 opening
            if loc2 not in opened and graph[loc2][0] > 0:
                key = (loc1, loc2, 0, 0, tuple(sorted(list(opened) + [loc2])))
                if t+1 not in dp: dp[t+1] = {}
                if key not in dp[t+1]: dp[t+1][key] = 0
                dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player1 opening and player1 staying stationary
            if loc1 not in opened and graph[loc1][0] > 0:
                key = (loc1, loc2, 0, 0, tuple(sorted(list(opened) + [loc1])))
                if t+1 not in dp: dp[t+1] = {}
                if key not in dp[t+1]: dp[t+1][key] = 0
                dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player1 and player2 both opening
            if loc1 != loc2 and loc1 not in opened and loc2 not in opened and graph[loc1][0] > 0 and graph[loc2][0] > 0:
                key = (loc1, loc2, 0, 0, tuple(sorted(list(opened) + [loc1,loc2])))
                if t+1 not in dp: dp[t+1] = {}
                if key not in dp[t+1]: dp[t+1][key] = 0
                dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player1 staying stationary and player2 moving
            for name, dist in graph[loc2][1]:
                if t+dist > TIMELIMIT: continue
                key = (loc1, name, 0, dist-1, opened)
                if t+1 not in dp: dp[t+1] = {}
                if key not in dp[t+1]: dp[t+1][key] = 0
                dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player1 moving and player2 staying stationary
            for name, dist in graph[loc1][1]:
                if t+dist > TIMELIMIT: continue
                key = (name, loc2, dist-1, 0, opened)
                if t+1 not in dp: dp[t+1] = {}
                if key not in dp[t+1]: dp[t+1][key] = 0
                dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player1 opening and player2 moving
            if loc1 not in opened and graph[loc1][0] > 0:
                for name, dist in graph[loc2][1]:
                    if t+dist > TIMELIMIT: continue
                    key = (loc1, name, 0, dist-1, tuple(sorted(list(opened) + [loc1])))
                    if t+1 not in dp: dp[t+1] = {}
                    if key not in dp[t+1]: dp[t+1][key] = 0
                    dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try player1 moving and player2 opening
            if loc2 not in opened and graph[loc2][0] > 0:
                for name, dist in graph[loc1][1]:
                    if t+dist > TIMELIMIT: continue
                    key = (name, loc2, dist-1, 0, tuple(sorted(list(opened) + [loc2])))
                    if t+1 not in dp: dp[t+1] = {}
                    if key not in dp[t+1]: dp[t+1][key] = 0
                    dp[t+1][key] = max(dp[t+1][key], score + flow)

            # Try both moving
            for name1, dist1 in graph[loc1][1]:
                for name2, dist2 in graph[loc2][1]:
                    if t+dist1 > TIMELIMIT: continue
                    if t+dist2 > TIMELIMIT: continue
                    key = (name1, name2, dist1-1, dist2-1, opened)
                    if t+1 not in dp: dp[t+1] = {}
                    if key not in dp[t+1]: dp[t+1][key] = 0
                    dp[t+1][key] = max(dp[t+1][key], score + flow)
    del dp[t]

print(best_score)
