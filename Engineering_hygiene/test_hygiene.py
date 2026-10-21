## pytest is a testing tool checking your function working well or not

import pytest
from calculator import add     ##if__name__ = __main__ concept using

@pytest.mark.parametrize(
    "a, b , expected",
    [
        (2,3,5),  # normal positive no's
        (0,0,0),  # zero case
        (-2, 5, 3),  # negative no's
        (10, -4, 6)  #mixed values
    ],
)

def test_add(a, b, expected):
    assert add(a,b) == expected