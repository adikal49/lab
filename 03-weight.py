#Ask a user their weight (in pounds),
#convert it to Kg and print on terminal

weight = input('What is your weight in pounds? ')
#formula 1 pounds * 0.45359237 = x kg
weight_in_kg = int(weight) * 0.45359237
print('weight in kg is', weight_in_kg)