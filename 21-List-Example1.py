#Write a program to find the largest number in a list.
numbers = [10, 30, 50, 20, 6, 8, 11]
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print(max)