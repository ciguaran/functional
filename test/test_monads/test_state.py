from functional.monads.state import State


def test_book_example():
    state = State(lambda state: state, "The state is {state}")
    assert state.run(10) == (10, "The state is 10")
    assert state.run_s(10) == 10
    assert state.run_a(10) == "The state is 10"


step_1 = State(lambda state: (state+1, f"Result of step1 {state+1}"))
step_2 = State(lambda state: (state*2, f"Result of step2 {state*2}"))


def two_steps_program(i):
    step_1.flat_map(lambda x: step_2)


def test_flat_map():
    step_1.flat_map(lambda x: step_2)


def test_get():
    get = State.get()
    assert get.run(10) == (10,10)


def test_set():
    set = State.set()
    assert set.run(20) == (20, None)


def test_modify():
    modify = State.modify(lambda state: state-10)
    assert modify.run(50) == (40, None)


def test_inspect():
    inspect = State.inspect(lambda x: x*50)
    assert inspect.run(20) == (20, 20*50)


def test_two_step_program():
    assert step_1.flat_map(step_2).run(10) == (22, "Result of step2 22")

class ForComprehension():
    """
    Simulates scala's for comprehension
    """

    def __init__(self):
        self.internal_state = {}

    def get_var(self, var_name):
        if var_name == "_":
            raise ValueError("_ is not a valid variable name")
        return self.internal_state[var_name]

    def __call__(self, asign_steps, yielding):
        """
        Emulates
        val both = for { a <- step1
                        b <- step2
                    } yield (a, b)

        by receiving
        :param asign_steps: [(str, monad)]
        :param yielding: (str,...,str)
        "_" is a special variable name indicating
        no storage is needed.
        """
        inner_state = {}
        for var, monad in asign_steps:
            



def test_for_comprehension():
    fc = ForComprehension()
    actual = fc(['a', State.get()],
                ('a',))



def test_program():
    """
    Example from page 121
    """
    monad = State.get()
    assert monad.run(1) == (1, 1)
    monad = monad.flat_map(State.set(lambda x: x+1))
    assert monad.run(1) == (2, None)
    monad = monad.flat_map(State.get())
    assert monad.run(1) == (2, 2)
    monad = monad.flat_map(State.modify(lambda x: x+1))
    assert monad.run(1) == (3, None)
    monad = monad.flat_map(State.inspect(lambda x: x*1000))
    assert monad.run(1) == (3, 3000)


