import sys

folder_stack = []
folder_contents = {}
folder_tree = {}
for line in sys.stdin:
    if not line.strip(): break
    cmds = line.strip().split()
    if cmds[0] == '$':
        # User command
        if cmds[1] == 'cd':
            # Change directory
            if cmds[2] == '..':
                folder_stack.pop()
            elif cmds[2] == '/':
                folder_stack.clear()
            else:
                folder_stack.append(cmds[2])
        elif cmds[1] == 'ls':
            # List
            pass
    else:
        # List output
        current_folder = tuple(folder_stack)
        if current_folder not in folder_contents: folder_contents[current_folder] = {}
        if current_folder not in folder_tree: folder_tree[current_folder] = {}

        if cmds[0] == 'dir':
            folder_tree[current_folder][cmds[1]] = None
        else:
            size = int(cmds[0])
            name = cmds[1]
            folder_contents[current_folder][name] = size

folder_sizes = {}

def calc_folder_sizes(current_folder = tuple()):
    assert current_folder in folder_tree
    for x in folder_tree[current_folder]:
        size = calc_folder_sizes(tuple(list(current_folder) + [x]))
        folder_tree[current_folder][x] = size

    assert current_folder in folder_contents
    size = sum(folder_contents[current_folder].values()) + sum(folder_tree[current_folder].values())
    folder_sizes[current_folder] = size
    return size

calc_folder_sizes()

size_used = folder_sizes[tuple()]
size_available = 70000000
size_necessary = 30000000
to_delete = size_necessary - (size_available - size_used)

folder_size_list = list(folder_sizes.items())
folder_size_list.sort(key = lambda x : x[1])
for folder,size in folder_size_list:
    if size >= to_delete:
        print(size)
        break
