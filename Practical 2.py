# Lab Assignment 1 – Ohm’s Law
V = float(input("Enter Voltage: "))
R = float(input("Enter Resistance: "))

I = V / R
print("Current =", I)

if I < 0.5:
    print("Low current")
elif I <= 2:
    print("Normal current")
else:
    print("High current")


# Lab Assignment 2 – Steel Grade
h = int(input("Enter hardness: "))
c = float(input("Enter carbon content: "))
t = int(input("Enter tensile strength: "))

cond1 = h > 50
cond2 = c < 0.7
cond3 = t > 5600

if cond1 and cond2 and cond3:
    grade = 10
elif cond1 and cond2:
    grade = 9
elif cond2 and cond3:
    grade = 8
elif cond1 and cond3:
    grade = 7
elif cond1 or cond2 or cond3:
    grade = 6
else:
    grade = 5

print("Grade =", grade)