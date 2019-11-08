class Graph:
    E = []

    def read(self, filename):
        with open(filename, 'r') as f:
            edges = f.readlines()
            for e in edges:
                e = e.split(" ")
                e = list(map(int, e))
                self.E.append(e)

    def adj(self, v, w):
        if [v, w] in self.E:
            return True
        else:
            return False

    def adj_edg(self, v):
        edges = []
        for e in self.E:
            if e[1] == v:
                edges.append(e)
        return edges

    def weight(self, v):
        counter = 0
        for e in self.E:
            if e[0] == v:
                counter += 1
        return counter

    def weight_edg(self, v, w):
        return (self.weight(v) + self.weight(w)) / 2

    def enum(self):
        for e in self.E:
            print(f"{e[0]}->{e[1]}")


