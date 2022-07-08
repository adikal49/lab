#Input Phone: & then print the numbers in words
numbers = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
phone =  input("Phone: ")
output = "" #Here we are adding out output to this empty string
for ch in phone:    
#print(numbers[f'{phone}'])
    output += numbers.get(ch, "!") + "  " #Here using get method if we to avoid errors
print(output)