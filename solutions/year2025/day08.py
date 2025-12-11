EXAMPLE_INPUT = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()

from math import sqrt

class UnionFind:
    def __init__(self, boxes):
        self.parent = list(boxes.keys())
        self.rank = [0]*len(self.parent)
        self.size = [1]*len(self.parent)
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False  # Already connected
        
        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.size[root_y] += self.size[root_x]
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            self.size[root_x] += self.size[root_y]
        return True  # Successfully merged
    
    def get_size(self, x):
        root = self.find(x)
        return self.size[root]
    
def find_distance(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return sqrt((ax-bx)**2 + (ay-by)**2 + (az-bz)**2)


def part1(data: str):
    """Solution for part 1."""
    data = [[int(x) for x in line.split(",")] for line in data.splitlines()]
    boxes = {}
    for i, row in enumerate(data):
        boxes[i] = tuple(row)

    distances = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            dist = find_distance(boxes[i], boxes[j])
            distances.append((dist, i, j))

    distances.sort()
    
    circuits = UnionFind(boxes)
    
    connections_made = 0
    idx = 0

    # while connections_made < 9 and idx < len(distances):
    for x in range(1000):
        dist, i, j = distances[idx]
        if circuits.union(i, j):
            connections_made += 1
            # print(f"Connection {connections_made}: boxes {i} and {j}, distance {round(dist, 1)}")
            # print(f"   {boxes[i]} | {boxes[j]}")
        idx += 1

    roots = [i for i in range(len(circuits.parent)) if circuits.parent[i] == i]
    # print(f"\nThere are now {len(roots)} circuits\n")
    sizes = []
    for root in roots:
        sizes.append(circuits.get_size(root))
        # print(f"The size of the circuit belonging to root {root} is {circuits.get_size(root)}")
    sizes.sort(reverse=True)
    # print(sizes)

    return sizes[0]*sizes[1]*sizes[2]

def part2(data: str):
    """Solution for part 2."""
    data = [[int(x) for x in line.split(",")] for line in data.splitlines()]
    boxes = {}
    for i, row in enumerate(data):
        boxes[i] = tuple(row)

    distances = []
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
            dist = find_distance(boxes[i], boxes[j])
            distances.append((dist, i, j))

    distances.sort()
    
    circuits = UnionFind(boxes)
    
    connections_made = 0
    idx = 0

    # while connections_made < 9 and idx < len(distances):
    for x in range(10000):
        dist, i, j = distances[idx]
        if circuits.union(i, j):
            connections_made += 1
            # print(f"Connection {connections_made}: boxes {i} and {j}, distance {round(dist, 1)}")
            # print(f"   {boxes[i]} | {boxes[j]}")
        idx += 1

        if x > 5000:
            roots = [i for i in range(len(circuits.parent)) if circuits.parent[i] == i]
            if len(roots) == 1:
                print(f"There is only one root left")
                print(boxes[i], boxes[j])
                return (boxes[i][0] * boxes[j][0])