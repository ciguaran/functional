from functional.monads.monads import Monad


class Option(Monad):
    @classmethod
    def some(cls, value):
        return Some(value)

    @classmethod
    def no_value(cls):
        return NoValue()

    @classmethod
    def pure(self, value):
        return Some(value)

    def flat_map(self, map_to_option):
        if self.has_value():
            return map_to_option(self.value)
        else:
            return self

    def has_value(self):
        pass


class NoValue(Option):
    def __init__(self):
        pass

    def has_value(self):
        return False

    def __eq__(self, other):
        return isinstance(other, NoValue)


class Some(Option):
    def __init__(self, value):
        self.value = value

    def has_value(self):
        return True

    def __eq__(self, other):
        return isinstance(other, Some) and other.value == self.value


def divide(a, b) -> Option:
    return NoValue() if (b == 0) else Some(a/b)


def parse_int(str) -> Option:
    try:
        to_return = Some(int(str))
    except ValueError:
        return NoValue()
    return to_return


def divide_strings(a_as_str: str, b_as_str: str) -> Option:
    return parse_int(a_as_str).flat_map(lambda a: parse_int(b_as_str).flat_map(lambda b: divide(a, b)))

