#ask hours worked
hours = float(input("How many hours did you work? "))
hourlyPay = 10
regularPay = hours * hourlyPay

if hours == 0:
        print("Here are job listings.")
else:
    if hours > 40:
        overtime = ((hours - 40) * 10) * 1.5
        pay = 400 + overtime
    else:
        pay = hours * 10


print("Pay: $", format(pay, ".2f"))


if hours == 0:
    print("Here are job listings.")
elif hours > 40:
        pay = hours * 10 + (10 * 1.5) * (hours - 40)
        print("Pay is $", format(pay, '.2f'), sep="")
else:
    pay = hours * 10
    print("Pay is $", format(pay, '.2f'), sep="")
#if hours = 45, pay should be $475.00
