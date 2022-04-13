from functional.monads.monads import Monad


class MonadicList(Monad):
    def __init__(self, value):
        super().__init__(value)


    def __eq__(self, other):
        return isinstance(other, MonadicList) \
               and other.value == self.value

    @classmethod
    def pure(cls, *arg):
        #A -> F[A]
        return MonadicList(arg)

    def flat_map(self, mapping):
        """
        (value: F[A])(func: A => F[B]): F[B]
        """
        return mapping(self.value)

    #def map(self, mapping):
    #    return MonadicList(list(map(mapping, self.underlying_list)))

