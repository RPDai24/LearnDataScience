# THis is Auto-graded Task 1

# Ask the user to enter a sentence
str_manip = input("Please enter a sentence : ")
# Calculate and display the length of str_manip.
manip_length = len(str_manip)
print(f"The sentence length : {manip_length}")
#Find the last letter
last_letter = str_manip[-1]
# replace the last letter with "@"
str_replace = str_manip.replace(last_letter, "@")
print("str_replace : " + str_replace)
# the last three characters backwards
str_last = str_manip[-3:]
str_last = str_last[::-1]
print("The last three characters : " + str_last)
print(str_manip[-1:-4:-1])
# Create a five-letter word
str_five = str_manip[0:3] + str_manip[-2:]
print("The five-letter word : " + str_five)