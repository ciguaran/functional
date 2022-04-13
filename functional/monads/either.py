from functional.monads.monads import Monad


class RightBiasedEither(Monad):
    def __init__(self, left, right):
        self.right = right
        self.left = left

    @classmethod
    def left(self, error):
        return RightBiasedEither(error, None)

    @classmethod
    def right(cls, val):
        return RightBiasedEither(None, val)

    @classmethod
    def pure(cls, val):
        return cls.right(val)

    def flat_map(self, value_to_monad):
        if self._is_right():
            return value_to_monad(self.right)

        else:
            return self

    def _is_right(self):
        return self.right is not None

    def get_or_else(self, other):
        if self._is_right():
            return self.right
        else:
            return other

    def ensure(self, msg, check):
        if self._is_right():
            if check(self.right):
                return self
            else:
                return RightBiasedEither.left(msg)
        else:
            return self

    def or_else(self):
        pass

    def recover(self):
        pass

    def recover_with(self):
        pass

    def left_map(self):
        pass

    def bi_map(self):
        pass

    def swap(self):
        pass

    def __eq__(self, other):
        return isinstance(other, RightBiasedEither) and self.left == other.left and self.right == other.right




