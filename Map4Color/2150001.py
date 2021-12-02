# name: Hiromu Ikemura
# id: 2150001
# acknowledgement: https://qiita.com/PondVillege/items/552b72e36126125074dd
# This article was written by me.

from PIL import Image
import sys

def product(x, y):
    return [(_x, _y) for _x in x for _y in y]

class UnionFind:
    def __init__(self, n, m):
        self.table = [[(-1, -1)] * n for _ in range(m)]
    
    def root(self, p):
        x, y = p
        stack = list()
        tbl = self.table
        while tbl[y][x] >= (0, 0):
            stack.append((x, y))
            x, y = tbl[y][x]
        for _x, _y in stack:
            tbl[_y][_x] = (x, y)
        return (x, y)
    
    def find(self, p1, p2):
        return self.root(p1) == self.root(p2)
    
    def union(self, p1, p2):
        r1 = self.root(p1)
        r2 = self.root(p2)
        if r1 == r2:
            return 
        
        d1 = self.table[r1[1]][r1[0]]
        d2 = self.table[r2[1]][r2[0]]
        if d1 <= d2:
            self.table[r2[1]][r2[0]] = r1
            if d1 == d2:
                self.table[r1[1]][r1[0]] = (self.table[r1[1]][r1[0]][0] - 1, self.table[r1[1]][r1[0]][1] - 1)
        else:
            self.table[r1[1]][r1[0]] = r2

class ImageProcessing:
    def __init__(self, img):
        self.img = img
        self.w, self.h = self.img.size
        self.uf = UnionFind(self.w, self.h)
        self.dgraph = dict()
        self.frame = set()
        self.fw = 5 # Frame Wdith
        self.color = [(255, 0, 0), (0, 0, 255), (0, 255, 0), (255, 0, 255)]
    
    def classify(self):
        for y, x in product(range(self.h - 1), range(self.w - 1)):
            if self.img.getpixel((x, y)) == (0, 0, 0):
                self.frame.add((x, y))
                continue
            for _x, _y in zip([x, x + 1], [y + 1, y]):
                if self.img.getpixel((x, y)) == self.img.getpixel((_x, _y)):
                    self.uf.union((x, y), (_x, _y))
            
            if x == 0:
                prg = 25 * y // self.h
                print("\r [{0}] {1:3}%".format("#" * prg + " " * (50 - prg), prg * 2), end="")
    
    def paint(self, colors):
        new = Image.new("RGB", (self.w, self.h))
        for y, x in product(range(self.h - 1), range(self.w - 1)):
            if (x, y) in self.frame:
                new.putpixel((x, y), (0, 0, 0))
                continue
            new.putpixel((x, y),
                self.color[colors.get(self.uf.root((x, y)), 0)]
            )
            if x == 0:
                prg = 10 * y // self.h + 40
                print("\r [{0}] {1:3}%".format("#" * prg + " " * (50 - prg), prg * 2), end="")
        new.save("a.png")
        print("\r [{0}] {1}%".format("#" * 50, 100))
    
    def graph(self):
        for y, x in product(range(self.h - self.fw), range(self.w - self.fw)):
            if (x, y) in self.frame or (x, y + self.fw) in self.frame or (x + self.fw, y) in self.frame:
                continue

            for _x, _y in zip([x, x + self.fw], [y + self.fw, y]):
                if not self.uf.find((x, y), (_x, _y)):
                    rx, ry = self.uf.root((x, y))
                    self.dgraph.setdefault((rx, ry), set())
                    self.dgraph[(rx, ry)].add(self.uf.root((_x, _y)))

            if x == 0:
                prg = 15 * y // self.h + 25
                print("\r [{0}] {1:3}%".format("#" * prg + " " * (50 - prg), prg * 2), end="")
        
        points = set()
        for key, value in self.dgraph.items():
            points.add(key)
            for v in value:
                points.add(v)
        
        for p in points:
            self.dgraph.setdefault(p, set())
            for key, value in self.dgraph.items():
                if key == p:
                    continue
                if p in value:
                    self.dgraph[p].add(key)

class Queue:
    def __init__(self, data = []):
        self.data = data
        self.lightly = set()

    def append(self, x):
        if x in self.lightly:
            return self.data
        else:
            self.data.append(x)
            self.lightly.add(x)
        return self.data
    
    def popleft(self):
        cell = self.data[0]
        self.lightly.discard(cell)
        del self.data[0]
        return cell

class Node:
    def __init__(self, point, nears):
        self.point = point
        self.nears = nears
        self.color = 0
    
    def __repr__(self):
        return f'Node index{self.point} nears:{self.nears} sign:{self.color}'

class Solver:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = dict()
        self.nc = 4
        for key, value in graph.items():
            self.nodes[key] = Node(key, value)
    
    def score(self):
        s = 0
        for key, value in self.graph.items():
            for v in value:
                if self.nodes[key].color == self.nodes[v].color:
                    s -= 1
        return s

    def solve(self):
        queue = Queue()
        for k in self.nodes.keys():
            queue.append(self.nodes[k])
        
        before, after = -1e8, -1e8
        while after != 0:
            node = queue.popleft()
            befcolor = node.color
            before = self.score()
            for i in range(self.nc - 1):
                self.nodes[node.point].color = (self.nodes[node.point].color + 1) % self.nc
                after = self.score()
                if before <= after:
                    break
            if before <= after:
                for near in node.nears:
                    queue.append(self.nodes[near])
            else:
                self.nodes[node.point].color = befcolor
            
            if not queue.data and after != 0:
                for k in self.nodes.keys():
                    queue.append(self.nodes[k])
        
        return {v.point: v.color for v in self.nodes.values()}
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You will need to execute with filename")
        sys.exit(-1)
    ip = ImageProcessing(Image.open(sys.argv[1]).convert("RGB"))
    ip.classify()
    ip.graph()
    solver = Solver(ip.dgraph)
    ip.paint(solver.solve())
