# Practical Task 1

# input a sentense
test_string = input("Please enter a sentense: ")
# test_string = "Hello World"
# test_string = "I am learning to code"

# each alternate character upper and lower
# list to store charachers
str_list = []
for i in range(len(test_string)):
    if i % 2 == 0:
       str_list.append(test_string[i].upper())
    else:
      str_list.append(test_string[i].lower())
#join to new string
new_str = "".join(str_list)  
print("New string 1: " + new_str)

# each alternative word lower and upper
word_list = test_string.split()
for i in range(len(word_list)):
   if i % 2 == 0:
      word_list[i] = word_list[i].lower()
   else:
      word_list[i] = word_list[i].upper()

new_word_str = " ".join(word_list)
print("New string 2: " + new_word_str)
