EXAMPLE_INPUT = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".strip()

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    # if start == end and "fft" in path and "dac" in path:
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    # print(paths)
    return paths

def part1(data: str):
    """Solution for part 1."""
    data = [line for line in data.splitlines()]
    data = [line.split(":") for line in data]

    graph = {}
    
    for device, cabling in data:
        cables = cabling.split()
        graph[device] = cables

    return len(find_all_paths(graph, 'you', 'out'))

def dfs_count(graph, node, end, fft=False, dac=False, visited=None, history=None):
    if visited is None:
        visited = set()
        history = {}
    
    if node in visited:
        return 0
    
    cache_key = (node, fft, dac)
    
    if cache_key in history:
        return history[cache_key]
    
    if node == end:
        result = 1 if (fft and dac) else 0
        history[cache_key] = result
        return result
    
    visited.add(node)
    
    total_paths = 0
    for child in graph[node]:
        fft_update = fft or child == "fft"
        dac_update = dac or child == "dac"
        total_paths += dfs_count(graph, child, end, fft_update, dac_update, visited, history)
    
    visited.remove(node)
    
    history[cache_key] = total_paths
    return total_paths


def part2(data: str):
    """Solution for part 2."""
    data = [line for line in data.splitlines()]
    data = [line.split(":") for line in data]

    graph = {}
    
    for device, cabling in data:
        cables = cabling.split()
        graph[device] = cables

    return dfs_count(graph, "svr", "out")