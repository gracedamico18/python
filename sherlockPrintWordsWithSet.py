#Exercise: sherlock.txt
#   Use a set to print all the words in the sherlock.txt file
#   Use a dictionary to print the frequency of each word

file = open('sherlock.txt', 'r')
sherlock = file.read()
file.close()

sherlock_list_of_words = sherlock.split()

sherlock_set = set(sherlock_list_of_words)
#could have used rstrip to get out all of the punctuation

print(sherlock_set)

for word in set_of_words:
    print(word)
input("...")





dict_of_words = {}
for word in words:
    if word not in dict_of_words:
        dict_of_words[word] = 1
    else:
        dict_of_words[word] = dict_of_words[word] + 1

for word in dict_of_words:
    print(  format(word, "18s"), \
            format(dict_of_words[word], "4d"))
