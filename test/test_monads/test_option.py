from functional.monads.option import divide_strings, Option, parse_int, divide


def test_divide_strings():
    assert divide_strings("hello", "1") == Option.no_value()
    assert divide_strings("hello", "hop") == Option.no_value()
    assert divide_strings("1", "hop") == Option.no_value()
    assert divide_strings("2", "2") == Option.some(1)


def test_parse_int():
    assert parse_int("2") == Option.some(2)
    assert parse_int("hello") == Option.no_value()


def test_pure():
    assert Option.pure(2) == Option.some(2)


def test_flat_map():
    assert Option.pure(2).flat_map(Option.pure) == Option.pure(2)
    assert Option.pure(2).flat_map(lambda x: Option.pure(4)) == Option.pure(4)
    assert Option.no_value().flat_map(lambda x: Option.pure(4)) == Option.no_value()


def test_map():
    assert Option.pure(2).map(lambda x: x * 2) == Option.pure(4)


def test_divide():
    assert divide(2,0) == Option.no_value()
    assert divide(2,2) == Option.some(1)

