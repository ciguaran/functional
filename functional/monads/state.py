from operator import add, mul
from functional.monads.monads import Monad



class State(Monad):

    def __init__(self, transformation):
        """
        Transformation
        State -> (State, Value)
        """
        #super().__init__(value)
        #self.state = state
        self.transformation = transformation

    def run(self, val):
        return self.transformation(val)

    def run_s(self, val):
        return self.transformation(val)[0]

    def run_a(self, val):
        return self.transformation(val)[1]

    def flat_map(self, another_state):
        """
        TODO This is different from inherited signature.
        :param another_state:
        :return:
        """
        """
        In this case value is of type (state, res) -> state
        :param value_to_monad:
        :return:
        """


        def compount_transformation(state):
            state, res = self.transformation(state)
            state, res = another_state.transformation(state)
            return state, res
        return State(compount_transformation)


    @classmethod
    def get(cls):
        """
        get extracts the state as the result;
        """
        return cls(lambda state: (state, state))

    @classmethod
    def set(cls, update):
        """
        set updates the state and returns unit as the result;
        """
        return cls(lambda state: (update(state), None))

    @classmethod
    def pure(cls, val):
        # TODO CHECK this doesn't seem LSP wrt base class
        return cls(lambda state: (state, val))

    @classmethod
    def inspect(cls, extraction):
        return cls(lambda state: (state, extraction(state)))

    @classmethod
    def modify(cls, mutation):
        return cls(lambda state: (mutation(state), None))



def parse(symbol):
    if symbol == "+":
        return add
    if symbol == "-":
        return lambda a,b: a-b
    if symbol == "*":
        return mul
    if symbol == "/":
        return lambda a,b: a/b
    else:
        return int(symbol)

def evalOne(symbol):
    return State(symbol, lambda x: [])



# def postfix_expression_parser():
#     to_parse = ["1","2","+"]
#     def mutate():
#         a = State(None, None, lambda val = ())

