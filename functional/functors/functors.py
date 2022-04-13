"""
Examples of functors
Option—the value may or may not be present;
Either—there may be a value or an error;
List—there may be zero or more values
Funciones de un solo parametro
"""
import typing
from abc import ABC, abstractmethod

"""
Interesante: futures vs IO type
Every example we’ve looked at so far is a functor: a class that encapsulates
sequencing computations.
"""
"""
def map[A, B](fa: F[A])(f: A => B): F[B]
"""
"""
Identity: calling map with the identity function is the same as doing noth‐
ing:
fa.map(a => a) == fa
Composition: mapping with two functions f and g is the same as
mapping with f and then mapping with g:
"""


class Functor(ABC):
    @abstractmethod
    def map(self, mapping):
        pass

    @abstractmethod
    def lift(self, f):
        pass

    @classmethod
    def lift(cls, mapping_non_functor):
        def lifted(functor):
            return functor.map(mapping_non_functor)

        return lifted


class Option(Functor):
    """
    Option is a functor
    """

    def __init__(self, inner_value):
        self.inner_value = inner_value

    def map(self, mapping):
        if self.inner_value is None:
            return self
        else:
            return Option(mapping(self.inner_value))

    def __eq__(self, other):
        return other.inner_value == self.inner_value


class Callable(Functor):
    """
    Functions from one parameter to one result
    are functors. Map is actually composition
    """

    def __init__(self, callable):
        self.callable = callable

    def map(self, mapping):
        return Callable(lambda x: mapping(self.callable(x)))

    def __call__(self, x):
        return self.callable(x)


def doMath(functor):
    return functor.map(lambda x: (x + 1) * 2)


class BinaryTree:
    pass


class Branch(BinaryTree, Functor):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def map(self, mapping):
        return Branch(self.left.map(mapping), self.right.map(mapping))

    def __eq__(self, other):
        return self.left == other.left and self.right == other.right


class Leaf(BinaryTree, Functor):
    def __init__(self, value):
        self.value = value

    def map(self, mapping):
        return Leaf(mapping(self.value))

    def __eq__(self, other):
        return self.value == other.value

A = typing.TypeVar('A')
B = typing.TypeVar('B`')

