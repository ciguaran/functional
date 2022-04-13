
class ContravariantFunctor:
    """
    In some sense functor allows to chain operators a->b->c
    Contravirant functor allows to add to begining of the chain
    aka having an a->b and c->a allow to get a c->a->b chain
    """
    def contramap(self, inverse):
        pass



class Printable(ContravariantFunctor):
    def __init__(self, format_function):
        self.format_function = format_function

    def format(self, value) -> str:
        return self.format_function(value)

    def contramap(self, inverse):
        # creating class dynamically

        def format_on_inverse_space(value):
            return self.format(inverse(value))

        inverted_printable = type("Printable", (object,), {
            # constructor
            #"__init__": constructor,

            # data members
            #"string_attribute": "Geeks 4 geeks !",
            #"int_attribute": 1706256,

            # member functions
            "format": format_on_inverse_space,
            "contramap": self.contramap
        })
        return inverted_printable





class StringPrintable(Printable):
    def format(self, value: str):
        return f"This is formated {value}"


class BooleanPrintable(Printable):
    def format(self, value: bool):
        return "SO TRUE" if value else "SO FALSE"
