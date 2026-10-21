import json
from pathlib import Path

def load_students(file_path: str) -> list[dict]:
    path = Path(file_path)

    try:
        with path.open("r", encoding= "utf-8") as file:
            students = json.load(file)

    except FileNotFoundError as error:
        raise PermissionError(
             f"इस file को read करने की permission नहीं है: {path}"
        ) from error

    except json.JSONDecodeError(students, list):
        raise ValueError(
            f"File में valid JSON नहीं है: {path}"
        ) from error

    if not isinstance(students, list):
        raise ValueError("JSON का top-level data एक list होना चाहिए")

    return students

try:
    students = load_students("students.json")
    print(f"{len(students)} students loaded")

except (FileNotFoundError, PermissionError, ValueError) as error:
    print(f"Error: {error}")
    raise  # program को fail loudly कराता है