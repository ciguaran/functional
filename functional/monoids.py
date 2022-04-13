class Semigroup:
    def __init__(self, operator):
        self.operator = operator

    def combine(self, x, y):
        return self.operator(x, y)


class Monoid(Semigroup):
    def __init__(self, empty, operator):
        super().__init__(operator)
        self.empty = empty

    def empty(self):
        return self.empty()


BooleanMonoidAnd = Monoid(True, lambda x, y: x and y)
BooleanMonoidOr = Monoid(False, lambda x, y: x or y)
SetsMonoidUnion = Monoid({}, lambda x, y: x.union(y))
SetSemigroupIntersection = Semigroup(lambda x, y: x.intersection(y))
