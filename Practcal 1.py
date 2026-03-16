# Lab Assignment 1 – Employee Salary

name = input("Enter name: ")
emp_id = input("Enter employee ID: ")
dept = input("Enter department: ")
basic = float(input("Enter basic salary: "))

da = 0.92 * basic
hra = 0.58 * basic
ta = 0.30 * basic
lic = 500

salary = basic + da + hra + ta - lic

print("Employee:", name)
print("Total Salary:", salary)


# Lab Assignment 2 – Vendor Annual Purchase
name = input("Vendor Name: ")
year = input("Year of Association: ")
contact = input("Contact Number: ")
email = input("Email: ")

total = 0
for i in range(12):
    purchase = float(input("Enter purchase for month: "))
    total += purchase
print("Annual Purchase:", total)