def greet(name: str) -> str:
    return f"Hello, {name}"

def calculate_average (numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)

def student_info(name: str, age: int, passed: bool) -> None:
    print(name, age, passed)