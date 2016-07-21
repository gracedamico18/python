#1. Display Welcome message.
print('Welcome to the 1089 trick!')

#2. Display About message.
about_message_1 = "This trick's sure to amaze your friends."
about_message_2 = """It's believed that the "1089 trick" was \
a favorite of Albert Einstein."""
about_message_3 = "To begin, enter a number with 3 digits, \
where the 1st digit and the 3rd digit differ by at least 2."
print(about_message_1, about_message_2, about_message_3)

#3. Input a number from the user.
number = int(input("Enter a number: "))

#4. Check that the number has 3 digits, and do not continue if not.
if (number < 100) or (number > 999):
    print("You must enter a 3-digit number.")
    quit()

#5. Check that the 1st digit and the 3rd digit differ by at least 2, 
#and do not continue if not.
firstDigit = number // 100
lastTwoDigits = number % (firstDigit * 100)

middleDigit = lastTwoDigits // 10
lastDigit = lastTwoDigits % (middleDigit * 10)

validSmallerFirstDigit = lastDigit - 2
validLargerFirstDigit = lastDigit + 2
validSmallerLastDigit = firstDigit - 2
validLargerLastDigit = firstDigit + 2

if (validSmallerFirstDigit < firstDigit < validLargerFirstDigit) or \
   (validSmallerLastDigit < lastDigit < validLargerLastDigit):
    print("The 1st digit and the 3rd digit must differ by at least 2.")
    quit()

#6. Calculate the reverse of the input.
reverse = (lastDigit * 100) + (middleDigit * 10) + (firstDigit) 

#7. Calculate the difference of the input and its reverse.
if (number < reverse):
    difference = reverse - number
else:
    difference = number - reverse

#8. Calculate the reverse of the difference.
digitOne = difference // 100
digitsTwoAndThree = difference % (digitOne * 100)

digitTwo = digitsTwoAndThree // 10
digitThree = digitsTwoAndThree % (digitTwo * 10)

reversed_difference = (digitThree * 100) + (digitTwo * 10) + (digitOne)

#9. Calculate the sum of the difference and its reverse.
result = difference + reversed_difference

#10. Output the results of the calculations.
print("The reverse of ", number, " is ", reverse, ".", sep="")
print("The difference of ", number, " and ", reverse, " is ", difference, ".", sep="")
print("The reverse of ", difference, " is ", reversed_difference, ".", sep="")
print("The sum of ", difference, " and ", reversed_difference, " is ", result, "!", sep="")


