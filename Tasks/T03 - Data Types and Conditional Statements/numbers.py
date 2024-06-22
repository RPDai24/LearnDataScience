# This is Auto-graded Task 2
# Ask the user to enter three different integers
num1 = int(input("Please enter a whole number : "))
num2 = int(input("Please enter a whole number : "))
num3 = int(input("Please enter a whole number : "))

# The sum of all the numbers
sum_num3 = sum([num1, num2, num3]) 
print(f"The sum of all the numbers: {sum_num3}")
# The first number minus the second number
print(f"The first number minus the second number: {num1 - num2}")
# The third number multiplied by the first number
print(f"The third number multiplied by the first number: {num3 * num1}")
# The sum of all three numbers divided by the third number
print(f"The sum of all three numbers divided by the third number: {sum_num3 / num3}")