student_name = input("whats your name : ")
math_score = float(input("whats your math score: "))
physics_score = float(input("whats your physics score: "))
english_score = float(input("whats your english score: "))
total = math_score + physics_score + english_score
average = total / 3
if average >= 90:
    grade = "A"
    remarks = "Excellent work!"
if average >= 80 and average < 90:
    grade = "B"
    remarks = "Good job!"
if average >= 70 and average < 80:
    grade = "C"
    remarks = "Keep it up!"
if average >= 60 and average < 70:
    grade = "D"
    remarks = "You can do better!"
if average < 60:
    grade = "F"
    remarks = "You need to improve!"
print(f"\nStudent Name: {student_name}")
print(f"Math Score: {math_score}")
print(f"Physics Score: {physics_score}")
print(f"English Score: {english_score}")
print(f"Total: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
print(f"Remarks: {remarks}")