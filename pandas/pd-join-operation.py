import pandas as pd

#FIRST PADAT FRAME
employees = pd.DataFrame({
    "employee_id": [101, 102, 103, 104],
    "name": ["Abhishek", "Rahul", "Priya", "Neha"],
    "department": ["AI", "BACKEND", "AI", "BACKEND"]
})

#SECOND DATA FRAME
salaries = pd.DataFrame({
    "employee_id": [101,102, 103, 105],
    "salary": [60000, 55000, 70000, 65000]
})

merged_df = employees.merge(salaries, on = "employee_id", how = "inner")

# inner_df = employees.merge(salaries, on= "employee_id", how = "inner")

left_df = employees.merge(salaries, on = "employee_id", how = "left" )

# print(left_df)

# print("Rows after left merge", len(left_df))

# print("Employees rows:", len(employees))
# print("Salaries rows:", len(salaries))
# print("Merged rows:", len(merged_df))

print(employees["employee_id"].duplicated().sum())
print(salaries["employee_id"].duplicated().sum())