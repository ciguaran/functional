from functional.functors.functors import Callable, Option, doMath, Branch, Leaf


def test_callable_functor():
    f = Callable(lambda x: x + 1)
    f = f.map(lambda x: x * 2)
    assert f(0) == 2
    assert f(1) == 4
    assert f(2) == 6


def test_option_functor():
    f = Option(None)
    f = f.map(lambda x: x + 1)
    assert f.inner_value is None
    f = Option(1)
    f = f.map(lambda x: x + 1)
    assert f.inner_value == 2
    f = Option(1)
    f = f.map(lambda x: None)
    assert f.inner_value is None


def test_do_math():
    """
    Do math is defined over any
    functor, so it works over Option,
    callable, etc.
    """
    assert doMath(Option(2)) == Option(6)
    f = doMath(Callable(lambda x: x + 1))
    assert f(2) == (2 + 1 + 1) * 2


def test_traverce_tree():
    binary_tree = Branch(Branch(Leaf(2), Leaf(3)), Leaf(3))
    assert binary_tree.map(lambda x: x + 1) == Branch(Branch(Leaf(3), Leaf(4)), Leaf(4))
