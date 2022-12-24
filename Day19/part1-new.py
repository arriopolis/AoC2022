import sys

blueprints = []
for line in sys.stdin:
    id, blueprint = line.strip().split(':')
    id = int(id.strip().split()[-1])
    robots = blueprint.strip().rstrip('.').split('.')
    blueprint = {}
    for robot in robots:
        robot = robot.split()
        type = robot[1]
        costs = dict(zip(robot[5::3], map(int,robot[4::3])))
        blueprint[type] = costs
    blueprints.append(blueprint)

TIMELIMIT = 24
total = 0
for j,blueprint in enumerate(blueprints):
    print("Investigating blueprint:", j+1, '/', len(blueprints))

    robots = {'ore' : 1, 'clay' : 0, 'obsidian' : 0, 'geode' : 0}
    resources = {'ore' : 0, 'clay' : 0, 'obsidian' : 0, 'geode' : 0}
    states = {tuple(sorted(robots.items())) : set([tuple(sorted(resources.items()))])}

    max_resources = {resource : max(cost[resource] for cost in blueprint.values() if resource in cost) for resource in ['ore', 'clay', 'obsidian']}

    running_best = 0

    for t in range(TIMELIMIT):
        print("Time step:", t, "with #states:", sum(map(len, states.values())))
        new_states = {}
        for robots, resource_combinations in states.items():
            robots = dict(robots)

            for resources in resource_combinations:
                resources = dict(resources)

                if resources['geode'] + sum(robots['geode'] + x for x in range(TIMELIMIT-t)) < running_best: continue

                # Add the no-building state
                new_resources = {resource : resources[resource] + robots[resource] for resource in resources}
                robots_key = tuple(sorted(robots.items()))
                if robots_key not in new_states: new_states[robots_key] = set()
                new_res = tuple(sorted(new_resources.items()))
                for res in new_states[robots_key].copy():
                    if all(a <= b for (_,a), (_,b) in zip(res, new_res)): new_states[robots_key].remove(res)
                    if all(a <= b for (_,a), (_,b) in zip(new_res, res)): break
                else:
                    new_states[robots_key].add(new_res)
                    running_best = max(running_best, new_resources['geode'] + robots['geode'] * (TIMELIMIT - t - 1))

                # Try building robots
                for type in resources:
                    if type in max_resources and resources[type] >= max_resources[type] and robots[type] >= max_resources[type]: continue
                    if all(blueprint[type][resource] <= resources[resource] for resource in blueprint[type]):
                        new_resources = {resource : resources[resource] - (blueprint[type][resource] if resource in blueprint[type] else 0) + robots[resource] for resource in resources}
                        new_robots = {type2 : robots[type2] + (1 if type2 == type else 0) for type2 in robots}
                        robots_key = tuple(sorted(new_robots.items()))
                        if robots_key not in new_states: new_states[robots_key] = set()
                        new_res = tuple(sorted(new_resources.items()))
                        for res in new_states[robots_key].copy():
                            if all(a <= b for (_,a), (_,b) in zip(res, new_res)): new_states[robots_key].remove(res)
                            if all(a <= b for (_,a), (_,b) in zip(new_res, res)): break
                        else:
                            new_states[robots_key].add(new_res)
                            running_best = max(running_best, new_resources['geode'] + new_robots['geode'] * (TIMELIMIT - t - 1))
        states = new_states
    print("Maximum #geodes:", running_best)
    total += (j+1) * running_best
print("Total:", total)
