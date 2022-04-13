from functional.monads.monadic_list import MonadicList


def test_monadic_list():
    # assert MonadicList([1,2,3,4]).map(lambda x: x*2) == MonadicList([2,4,6,8])
    # assert MonadicList([]).map(lambda x:x*2) == MonadicList([])
    # assert MonadicList.pure() == MonadicList([])
    assert MonadicList.pure(1) == MonadicList([1])
    assert MonadicList.pure(1,2,3,4) == MonadicList([1,2,3,4])
    assert MonadicList([1,2,3,4]).flat_map(MonadicList.pure) == MonadicList([1,2,3,4])


def test_left_identity():
    assert MonadicList.pure([1,2,3]).flat_map(multiply_by_two) == multiply_by_two([1,2,3])


def test_right_identity():
    assert MonadicList([1,2,3]).flat_map(MonadicList.pure) == MonadicList([1,2,3])


def test_associativity():
    actual =  MonadicList([1,2,3]).flat_map(multiply_by_two).flat_map(sum_3)
    expected = MonadicList([1,2,3]).flat_map(lambda x: multiply_by_two(x).flat_map(sum_3))
    assert actual == expected


def multiply_by_two(ml):
    return MonadicList(ml).map(lambda x:x*2)

def sum_3(ml):
    return MonadicList(ml).map(lambda x:x+3)