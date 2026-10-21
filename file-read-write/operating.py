import os

if (not os.path.exists("data")):
    os.mkdir("Data")

for i in range(0, 101):
    os.rename(f"data/day{i+1}", f"Data/Tutorial{i+1}")


print(os.getcwd())

