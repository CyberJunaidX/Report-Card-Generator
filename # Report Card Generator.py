# Report Card Generator

name = input("Enter student name: ")
num_subjects = int(input("How many subjects? :"))

subjects = {}

for i in range(num_subjects):
    subject = input(f"Enter subject {i+1} name: ")
    marks = float(input(f"Enter marks for {subject}: "))
    subjects[subject] = marks

total = sum(subjects.values())
average = total / num_subjects

print("\n----- REPORT CARD -----")
print("Name:", name)
for subject, marks in subjects.items():
    print(subject, ":", marks)

print("Total:", total)
print("Average:", average)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("Grade:", grade)