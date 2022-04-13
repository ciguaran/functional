from functional.functors.contravariant_functor import Printable


def test_printable():
    p = Printable(lambda x: f"printed by printable {x}")
    assert p.format(2) == "printed by printable 2"
    p = p.contramap(lambda x: x==2)
    assert p.format(2) == "printed by printable True"
    assert p.format(3) == "printed by printable False"
