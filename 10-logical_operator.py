#if the applicant has high income & good credit
#he is eligible for loan

#operators list
#and : both
#or : atleast one
#not : 
'''
high_income = True
good_credit = False
if high_income or good_credit:
    print('Person is eligible for loan')
else:
    print('Person is not eligible for loan')
'''

print('############################################')
 #if the applicant has a good credit & doesnt have a criminal record
good_credit = True
has_criminal_record = True 
#This will inverse in "not" & with "and" we will has one true & one false
if good_credit and not has_criminal_record:
    print('Person is eligible for loan')
else:
    print('Person is not eligible for loan')