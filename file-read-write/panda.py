import csv 

## write csv

with open("users.csv", 'w', newline ="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age", "city"])
    writer.writerow(["Abhishek", 28, "Delhi"])
    writer.writerow(["Rahul", 27, "Ranchi"])

#Read csv

with open("users.csv", 'r', newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)