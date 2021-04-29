with open("puzzle_input.txt", 'r') as f:
    orbits = [line.strip() for line in f.readlines()]


class Node:
    all = dict()

    @classmethod
    def factory(cls, name, *args, **kwargs):
        if name in Node.all:
            return Node.all[name]
        else:
            return Node(name, *args, **kwargs)

    def __init__(self, name, parent=None):
        self.parent = parent
        self.name = name
        self.children = []
        Node.all[self.name] = self

    def __repr__(self):
        return self.name

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_depth(self):
        if self.parent:
            return self.parent.get_depth() + 1
        else:
            return 0

    def get_path(self):
        if self.parent:
            return self.parent.get_path() + [self]
        else:
            return [self]

    def __hash__(self):
        return hash(self.name)


for orbit in orbits:
    o1, o2 = orbit.split(")")
    Node.factory(o1).add_child(Node.factory(o2))

# s = sum([node.get_depth() for node in Node.all.values()])
# print(s)

YOU_path = set(Node.factory('YOU').get_path())
SAN_path = set(Node.factory('SAN').get_path())
symmetric_difference_path = YOU_path.symmetric_difference(SAN_path)
print(len(symmetric_difference_path))
