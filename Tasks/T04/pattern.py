# Practical Task 2
#
stars = ""
# Output the pattern
for i in range(0, 10):
    stars = stars + "*"
    if len(stars) <= 5:
        print(stars)
    else:
        # print(10-len(stars))
        print(stars[0 : 10 - len(stars)])

