gender = str(input("Are you male or female? Enter in lowercase letters. "))
if (gender == 'male'):
    age = int(input("Enter your age: "))
    if (16 <= age <= 20):
        print("Your car insurance rate is $725.")
    elif (21 <= age <= 25):
        print("Your car insurace rate is $500.")
    elif (26 <= age <= 30):
        print("Your car insurace rate is $375.")
    else:
        print("Your car insurance rate is $180.")
else:
    age = int(input("Enter your age: "))
    if (16 <= age <= 20):
        print("Your car insurance rate is $525.")
    elif (21 <= age <= 25):
        print("Your car insurace rate is $375.")
    elif (26 <= age <= 30):
        print("Your car insurace rate is $300.")
    else:
        print("Your car insurance rate is $180.")
    
