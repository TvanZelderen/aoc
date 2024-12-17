EXAMPLE_INPUT = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip()

def part1(data: str):
    """Solution for part 1."""
    data = [line for line in data.splitlines()]
    rows = len(data)
    cols = len(data[0])

    zeros = set()
    graph = {}

    hikes = set()

    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for r, row in enumerate(data):
        for c, char in enumerate(row):
            char = int(char)
            if char == 9:
                continue
            if char == 0:
                zeros.add((r, c))
            graph[(r, c)] = []
            for direction in directions:
                # print(r, c, r + direction[0], c + direction[1])
                # print(int(data[r + direction[0]][c + direction[1]]))
                # print(int(data[r + direction[0]][c + direction[1]]) == char + 1)
                # print(((r + direction[0]) > 0))
                # print(((c + direction[1]) > 0))
                if (0 <= (r + direction[0]) < rows) and (0 <= (c + direction[1]) < cols) and int(data[r + direction[0]][c + direction[1]]) == char + 1:
                    graph[(r, c)].append((r + direction[0], c + direction[1]))

    def dfs(visited, graph, node):
        if node not in visited:
            # print(f"DFS:{node}")
            visited.add(node)
            for neighbour in graph[node]:
                # print(f"Neighbour {neighbour}, {data[neighbour[0]][neighbour[1]]}")
                try:
                    dfs(visited, graph, neighbour)
                except KeyError:
                    r, c = neighbour
                    if int(data[r][c]) == 9:
                        hikes.add((zero, (r, c)))


    for zero in zeros:
        visited = set()
        dfs(visited, graph, zero)

    return len(hikes)


def part2(data: str):
    """Solution for part 2."""
    data = [line for line in data.splitlines()]
    rows = len(data)
    cols = len(data[0])

    zeros = set()
    graph = {}

    hikes = {}

    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for r, row in enumerate(data):
        for c, char in enumerate(row):
            char = int(char)
            if char == 9:
                continue
            if char == 0:
                zeros.add((r, c))
            graph[(r, c)] = []
            for direction in directions:
                # print(r, c, r + direction[0], c + direction[1])
                # print(int(data[r + direction[0]][c + direction[1]]))
                # print(int(data[r + direction[0]][c + direction[1]]) == char + 1)
                # print(((r + direction[0]) > 0))
                # print(((c + direction[1]) > 0))
                if (0 <= (r + direction[0]) < rows) and (0 <= (c + direction[1]) < cols) and int(data[r + direction[0]][c + direction[1]]) == char + 1:
                    graph[(r, c)].append((r + direction[0], c + direction[1]))

    def dfs(visited, graph, node):
        # if node not in visited:
            # print(f"DFS:{node}")
        visited.add(node)
        for neighbour in graph[node]:
            try:
                dfs(visited, graph, neighbour)
            except KeyError:
                r, c = neighbour
                if int(data[r][c]) == 9:
                    if zero not in hikes: hikes[zero] = []
                    hikes[zero].append((r, c))


    for zero in zeros:
        visited = set()
        dfs(visited, graph, zero)


    len_hikes = 0
    for hike in hikes:
        len_hikes += len(hikes[hike])

    return len_hikes