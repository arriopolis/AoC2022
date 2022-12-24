import sys
import itertools as it

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

total = 0
extra_info = {}
for j,blueprint in enumerate(blueprints):

    # DEBUG
    # if j != 1: continue

    print("Investigating blueprint:", j+1, '/', len(blueprints))

    robots = {'ore' : 1, 'clay' : 0, 'obsidian' : 0, 'geode' : 0}
    resources = {'ore' : 0, 'clay' : 0, 'obsidian' : 0, 'geode' : 0}

    max_resources = {resource : max(cost[resource] for cost in blueprint.values() if resource in cost) for resource in ['ore', 'clay', 'obsidian']}

    states = {tuple(sorted(robots.items())) : set([tuple(sorted(resources.items()))])}

    for t in range(24):
        print("Time step:", t, "with #states:", sum(map(len, states.values())))
        # print(states)
        new_states = {}
        for robots, resource_combinations in states.items():
            robots = dict(robots)

            for resources in resource_combinations:
                resources = dict(resources)

                if any(robots[resource] > max_resources[resource] and resources[resource] >= max_resources[resource] for resource in ['ore', 'clay', 'obsidian']): continue

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
                    extra_info[(t, robots_key, new_res)] = (t-1, tuple(sorted(robots.items())), tuple(sorted(resources.items())))

                # Try building robots
                build_robots = {type : 0 for type in robots}
                while True:
                    for type in sorted(build_robots.keys()):
                        build_robots[type] += 1

                        required_resources = {type : 0 for type in resources}
                        for build_type, num in build_robots.items():
                            for resource, amount in blueprint[build_type].items():
                                required_resources[resource] += amount * num

                        if sum(build_robots.values()) <= 1 and all(required_resources[resource] <= resources[resource] for resource in resources):
                            new_resources = {resource : resources[resource] - required_resources[resource] + robots[resource] for resource in resources}
                            new_robots = {type : robots[type] + build_robots[type] for type in robots}
                            robots_key = tuple(sorted(new_robots.items()))
                            if robots_key not in new_states: new_states[robots_key] = set()
                            new_res = tuple(sorted(new_resources.items()))
                            for res in new_states[robots_key].copy():
                                if all(a <= b for (_,a), (_,b) in zip(res, new_res)): new_states[robots_key].remove(res)
                                if all(a <= b for (_,a), (_,b) in zip(new_res, res)): break
                            else:
                                new_states[robots_key].add(new_res)
                                extra_info[(t, robots_key, new_res)] = (t-1, tuple(sorted(robots.items())), tuple(sorted(resources.items())))
                            break
                        else:
                            build_robots[type] = 0
                    else: break
        states = new_states

    best_blueprint = 0
    for robots, resource_combinations in states.items():
        for resources in resource_combinations:
            resources = dict(resources)
            best_blueprint = max(best_blueprint, resources['geode'])

            # DEBUG
            # if resources['geode'] == 13:
            #     state = (23, robots, tuple(sorted(resources.items())))
            #     history = [state]
            #     while state in extra_info:
            #         state = extra_info[state]
            #         history.append(state)
            #     history.reverse()
            #     for t, robots, resources in history:
            #         robots = dict(robots)
            #         resources = dict(resources)
            #         print(*map(lambda x : '{:>3s}'.format(str(x)), [
            #                 t+1,
            #                 resources['ore'], resources['clay'], resources['obsidian'], resources['geode'],
            #                 robots['ore'], robots['clay'], robots['obsidian'], robots['geode']
            #             ])
            #         )
            #     print()
    # sys.exit()
    print("Maximum #geodes:", best_blueprint)

    quality_score = (j+1) * best_blueprint
    print("Quality score:", quality_score)

    total += quality_score
print("Total:", total)
