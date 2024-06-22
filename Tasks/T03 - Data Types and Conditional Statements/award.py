# This is Auto-graded Task 3
# Read the times for a triathlon
swimming_time = float(input("Please tell us your swimming time(in minutes): "))
cycling_time = float(input("Please tell us your swimming time(in minutes): "))
running_time = float(input("Please tell us your swimming time(in minutes): "))
# Calculate the total time float
total = sum([swimming_time, cycling_time, running_time])
print(f"the triathlon total time(float): {total}")
# Round the total time to int
total_time = round(total)
print(f"the triathlon total time(int): {total_time} ")
# Are you win the triathlon award?
if total_time>0 and total_time <= 100:
    print("Congratulations,you have won Provincial colours!")
elif total_time >= 101 and total_time <= 105:
    print("Congratulations,you have won Provincial half colours!")
elif total_time >= 106 and total_time <= 110:
    print("Congratulations,you have won Provincial scroll!")
elif total_time >=111:
    print("No award")
else:
    print("Some thing wrong or No participate.")





