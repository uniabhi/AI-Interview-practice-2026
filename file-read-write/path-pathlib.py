## 1. os.path (way)

import os

# folder = "Python_test_2026"

# filename = "users.csv"

# path = os.path.join(folder, filename)

# print(path)

# path = "users.csv"

# print(os.path.basename(path))
# print(os.path.splitext(path)[1])
# print(os.path.dirname(path))


# ## 2. pathlib way

from pathlib import Path

# folder = Path("Python_test_2026")

# filename = "users.csv"

# path = folder / filename

# print(path)

# ## 3rd
# path = Path("users.csv")
# print(type(path))

# print(path.exists())
# print(path.name)
# print(path.suffix)
# print(path.parent)

# if os.path.exists("users.csv"):
#     print("file exists")


# path = Path("users.csv")
# if path.exists():
#     print("File Exists")


# from pathlib import Path
# path = Path("abhi_folder_2026/data")
# path.mkdir(parents=True, exist_ok=True)

from pathlib import Path

base_dir = Path("project")

train_dir = base_dir / "data" / "train"
val_dir = base_dir / "data" / "validation"
model_dir = base_dir / "model"

print(train_dir)
print(val_dir)
print(model_dir)