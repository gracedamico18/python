
def newUser():
    name = input("What is your name? ")
    birthday = input("What is your birthday? ")

    nameBirthday = open('name_birthday.txt', 'w')
    nameBirthday.write(name + "\n")
    nameBirthday.write(birthday)
    nameBirthday.close()
    return name, birthday

def main():
    try:
        openFile = open("name_birthday.txt", 'r')
    except FileNotFoundError:
        print("Sorry the file doesn't exist. One is being created for you.")
        name, birthday = newUser()
    except (PermissionError, IsADirectoryError) as error:
        print("Could not read file")
        print(error)
        quit()
    #this is a generic exception which will quit program 
    #regardless of what error it is
    except:
        print("Could not read file")
        quit()
    else:
        name = openFile.readline()
        name = name.rstrip('\n')
        birthday = openFile.readline()
        openFile.close()
        
    print("Welcome, ", name, ", what is today's date? ", sep="")
    date = input()

    if date == birthday:
        print("Happy Birthday!")
    else:
        print("Sorry today is not your birthday :( ")


#rm name_birthday.txt ----- this removes the file from command line
main()
