#Write a program to remove duplicates in a list
numbers = [5, 2, 30, 7 , 4, 5, 2 ,7, 20]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

