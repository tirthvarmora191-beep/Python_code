name = input("Enter student name: ")

maths = float(input("Enter Maths marks: "))
physics = float(input("Enter Physics marks: "))
python = float(input("Enter Python marks: "))
english = float(input("Enter English marks: "))

total = maths + physics + python + english
percentage = total / 4

print("\n----- Result -----")
print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)

if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: F")