# Practical Task 2
# how many students are registering
num_students = int(input("How many students are registering?\n"))
# number less than 0 iterate to input
while num_students <= 0:
    num_students = int(input("How many students are registering?\n"))
# store students ID
student_id_str = ""
for i in range(num_students):
    student_id = input(f"Please enter the student ID number ({i + 1}): ")
    student_id_str = student_id_str + student_id + ".....................\n"
# write students ID to reg_form.txt
with open("reg_form.txt", "w") as file:
    file.write(student_id_str)
