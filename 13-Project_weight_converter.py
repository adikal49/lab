#Weight_converter
#Enter weight 
#ask either in (L)bs or (K)g
#print weight in another unit
weight = input("What is your weight? ")
units = input("(L)bs or (K)g: ")

if (units.lower() == 'l'):
    kgs = float(weight) * 0.45 #Not using int bcoz if decimal we get error
    print(f'weight in kilos is {kgs} kg')
else:
    #lbs = int(weight) // 0.45
    lbs = float(weight) / 0.45 #Not using int bcoz if decimal we get error
    print(f'weight in pounds is {lbs} lbs')