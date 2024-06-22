# Practical Task 1

# store the names
name_str = "Name\n"
# store the birthdates
birthdate_str = "Birthdate\n"
# open DOB.txt
with open("./Input Code Files/Task file/DOB.txt", "r") as file:
    # iterate read line
    for line in file:
        # split line by whitespace
        line_list = line.split()
        name_str = name_str + line_list[0] + " " + line_list[1] + "\n"
        birthdate_str = birthdate_str + line_list[2] + " " + line_list[3] + " " + line_list[4] + "\n"

print(name_str)
print(birthdate_str)
