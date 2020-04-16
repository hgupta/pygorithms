class Vector(object):
    def __init__(self, data):
        if isinstance(data, (tuple, list)):
            self.l = tuple(float(e) for e in data)
        elif isinstance(data, Vector):
            self.l = tuple(e for e in data.l)

    def inner(self, other):
        return sum(e1 * e2 for e1, e2 in zip(self, other))

    def __add__(self, other):
        return Vector(tuple(e1 + e2 for e1, e2 in zip(self, other)))

    def __sub__(self, other):
        return Vector(tuple(e1 - e2 for e1, e2 in zip(self, other)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.inner(other)

        assert isinstance(other, (int, float))
        return Vector(tuple(e * other for e in self))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        assert isinstance(other, (int, float))
        return Vector(tuple(float(e / other) for e in self))

    def __len__(self):
        return len(self.l)

    def __getitem__(self, key):
        return self.l[key]

    def __iter__(self):
        return self.l.__iter__()

    def __repr__(self):
        return f'<Vector l=({", ".join(str(e) for e in self.l)})>'



v1 = Vector((1,2,3,4))
print(v1)
v2 = Vector(v1)
print(v2[3])

print(v1 + v2)
