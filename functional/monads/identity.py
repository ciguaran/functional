
class Id(Monad):
    def __init__(self, value):
        self.value = value

    @classmethod
    def pure(self, value):
        return Id(value)

    def map(self, mapping):
        return Id(mapping(self.value))

    def flatMap(self, mapping):
        return Id(mapping(self.value))

