from pathlib import Path

folder = Path("Data")

for file in folder.rglob("*.csv"):
    print(file)