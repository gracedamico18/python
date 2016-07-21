#Grace D'Amico
#Project 3 - Cipher

import string
import pickle
import random

#Activity 1 - CHECKED
def main():
    cipher_object = Cipher()
    choice = 0
    while choice != 6:
        choice = menu()

        if choice == 1:
            infile = input("Enter the input file name: ")
            outfile = input("Enter the output file name: ")
            cipher_object.encrypt(infile, outfile)

        elif choice == 2:
            infile = input("Enter the input file name: ")
            outfile = input("Enter the output file name: ")
            cipher_object.decrypt(infile, outfile)

        elif choice == 3:
            cipher_object.shuffle()

        elif choice == 4:
            outfile = input("Enter the file name: ")
            cipher_object.save(outfile)

        elif choice == 5:
            infile = input("Enter the file name: ")
            cipher_object = cipher_object.restore(infile)
    else:
        quit()
    
def menu():
    choice = 0
    print("1) Encrypt a file")
    print("2) Decrypt a file")
    print("3) Shuffle key")
    print("4) Save cipher state")
    print("5) Restore cipher state")
    print("6) Quit")

    error = True
    while error == True:
        try:
            choice = int(input("Enter your choice: "))
            error = False
            while choice > 6 or choice < 1:
                choice = input("Choice needs to be 1-6. ")
                error = False
        except ValueError:
            print("Must enter an integer. ", end="")
            error = True
        except TypeError:
            print("Choice needs to be 1-6. ", end="")
            error = True
    return choice



#Activity 2-3 - CHECKED
class Cipher():
    
    #Activity 6 - NOT CHECKED
    def __init__(self):
        self.key = {'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'H':'H', 'I':'I', 'J':'J', \
               'K':'K', 'L':'L', 'M':'M', 'N':'N', 'O':'O', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', \
               'U':'U', 'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z'}

    #Activity 5 - DONE - NOT CHECKED
    #ACT 6 -encrypt method should replace each letter with key[letter].
    def encrypt(self, infile, outfile):
        error = True
        while error == True:
            try:
                infile = open(infile, 'r')
                error = False
            except FileNotFoundError:
                print("Input file not found. Enter valid file name: ", end="")
                infile = input()
                error = True
        while error == True:
            try:
                outfile = open(outfile, 'w')
                error = False
            except FileNotFoundError:
                print("Output file not found. Enter valid file name: ", end="")
                outfile = input()
                error = True
        text = infile.read()
        alphabet_upper = string.ascii_uppercase
        alphabet_lower = string.ascii_lowercase
        
        for i in range(len(text)):
            if text[i].isdigit() or text[i].isspace():
                outfile.write(text[i])
            else:
                letter = text[i]
                if letter.islower():
                    alphabet_index = alphabet_lower.find(letter)
                    encrypt_index = alphabet_index + self.key
                    if encrypt_index >= 26:
                        encrypt_index = encrypt_index % 26
                    encrypt_letter = alphabet_lower[encrypt_index]
                    outfile.write(encrypt_letter)
                else:
                    alphabet_index = alphabet_upper.find(letter)
                    encrypt_index = alphabet_index + self.key
                    if encrypt_index >= 26:
                        encrypt_index = encrypt_index % 26
                    encrypt_letter = alphabet_upper[encrypt_index]
                    outfile.write(encrypt_letter)
        infile.close()
        outfile.close()



    #ACT 6 - decrypt method should replace each letter with whichever original maps to letter
    #(i.e., letter should be mapped to original where key[original] = letter)
    def decrypt(self, infile, outfile):
        error = True
        while error == True:
            try:
                infile = open(infile, 'r')
                error = False
            except FileNotFoundError:
                print("Input file not found. Enter valid file name: ", end="")
                infile = input()
                error = True
        while error == True:
            try:
                outfile = open(outfile, 'w')
                error = False
            except FileNotFoundError:
                print("Output file not found. Enter valid file name: ", end="")
                outfile = input()
                error = True
        text = infile.read()
        alphabet_upper = string.ascii_uppercase
        alphabet_lower = string.ascii_lowercase
        
        for i in range(len(text)):
            if text[i].isdigit() or text[i].isspace():
                outfile.write(text[i])
            else:
                letter = text[i]
                if letter.islower():
                    alphabet_index = alphabet_lower.find(letter)
                    decrypt_index = alphabet_index - self.key
                    if decrypt_index < 0:
                        decrypt_index = decrypt_index + 26
                    decrypt_letter = alphabet_lower[decrypt_index]
                    outfile.write(decrypt_letter)
                else:
                    alphabet_index = alphabet_upper.find(letter)
                    decrypt_index = alphabet_index - self.key
                    if decrypt_index < 0:
                        decrypt_index = decrypt_index + 26
                    decrypt_letter = alphabet_upper[decrypt_index]
                    outfile.write(decrypt_letter)
        infile.close()
        outfile.close()


    #Activity 4 - DONE - NOT CHECKED
    #Activity 6 - DONE - NOT CHECKED
    def shuffle(self):
        alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', \
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', \
                         'W', 'X', 'Y', 'Z' ]
        permutation = random.shuffle(alphabet_list)


        
    def save(self, outfile):
        pickle_dump_file = open(outfile, 'wb')
        pickle.dump(self, pickle_dump_file)
        pickle_dump_file.close()

    @classmethod
    def restore(cls, infile):
        load_file = open(infile, 'rb')
        pickle_load = pickle.load(load_file)
        load_file.close()
        return pickle_load




main()
