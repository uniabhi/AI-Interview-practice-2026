# test_student.py
import pytest
from student import Student

@pytest.fixture
def pass_marks():
    return 40

@pytest.mark.parametrize(
    "marks, expected",
    [
        (75, True),
        (40, True),
        (39, False),
        (0, False),
    ],
)
def test_is_passed(pass_marks, marks, expected):
    student = Student(
        name="Abhishek",
        marks=marks,
        pass_marks=pass_marks,
    )

    assert student.is_passed() == expected