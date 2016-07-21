#Determine average number of words per sentence from sherlock.txt file.

sherlock = open("sherlock.txt", "r")
sherlock_contents = sherlock.read()
sherlock.close()

#all content of file is now in a list.
#Each item in the list is a sentence.
sentence = sherlock_contents.split(".")

#len(sherlock_contents.split()) = # words
#sherlock_contents.split() = list of words
#sherlock_contents.split(".") = list of sentences
#len(sherlock_contents.split(".") = # sentences
print(len(sherlock_contents.split()) / len(sherlock_contents.split(".")))

