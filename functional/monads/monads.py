
from abc import ABC, abstractmethod
from functional.functors.functors import Functor





class Monad(Functor, ABC):
    """
    In practice: monad is mechanism for sequencing computations. Functors can
    also do that, but monads allow to have logic on erros in each step.

    In a statically typed system we would have:
    pure: A => F[A];
    flatMap: (F[A], A => F[B]) => F[B].

    It should hold that:
    Monad Laws
    pure and flatMap must obey a set of laws that allow us to sequence operations freely without unintended glitches and side‐effects:

    Left identity: calling pure and transforming the result with func is the same as calling func:

    pure(a).flatMap(func) == func(a)

    Right identity: passing pure to flatMap is the same as doing nothing: m.flatMap(pure) == m

    Associativity: flatMapping over two functions f and g is the same as flatMapping over f and then flatMapping over g:

    m.flatMap(f).flatMap(g) == m.flatMap(x => f(x).flatMap(g))

    """
    def __init__(self, value):
        self.value = value

    @classmethod
    def pure(cls, value):
        return cls(value)

    @abstractmethod
    def flat_map(self, value_to_monad):
        raise NotImplementedError

    def map(self, mapping):
        return self.flat_map(lambda x: self.pure(mapping(x)))




