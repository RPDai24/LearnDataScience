# Practical Task 1


# count of the numbers
i = 0
# Sum of the mubers
sum = 0
# While loop conditon true, so continually asks the user to enter a number
while True:
    # Ask user to enter a number
    num = int(input("Please enter a number: "))
    if num == -1:
        print("Break the while loop.")
        break
    else:
        sum += num
        i += 1
print(f"sum: {sum} i: {i}")
# canculate the average
if i > 0:
     average = sum / i
     print(f"Average of all the numbers: {average}")
else:
     print("You didn't enter any numbers.")
     


