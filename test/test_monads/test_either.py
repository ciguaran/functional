from functional.monads.either import RightBiasedEither


def test_pure():
    assert RightBiasedEither.right(1) == RightBiasedEither.pure(1)


def test_map():
    assert RightBiasedEither.right(1).map(lambda x: x*2) == RightBiasedEither.right(2)
    assert RightBiasedEither.left("error").map(lambda x: x*2) == RightBiasedEither.left("error")


def test_flat_map():
    def check_positive(x):
        return RightBiasedEither.right(x) if x > 0 else RightBiasedEither.left("this is wrong")

    assert RightBiasedEither.right(2).flat_map(check_positive) == RightBiasedEither.right(2)
    assert RightBiasedEither.right(-12).flat_map(check_positive) == RightBiasedEither.left("this is wrong")
    assert RightBiasedEither.left("error").flat_map(check_positive) == RightBiasedEither.left("error")