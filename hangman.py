# evilhangman.py
# simple game of hangman, except the computer cheats undetectably

import string

# letters successfully guessed saved here
# integer maps to character by position in the word
knownLetters = dict()

# all letters that have been guessed, including dodged letters
guessedLetters = dict()

def filterLen(size, l):
	newList = []
	for w in l:
		if len(w) == size:
			newList.append(w)
	return newList

def filterChar(pos, c, l):
	newList = []
	for w in l:
		if w[pos] != c:
			newList.append(w)
	return newList

def filterWords(pos, c, l):
	newList = []
	for w in l:
		valid = True
		for i in pos:
			if w[i] != c:
				valid = False
				break
		if valid == True:
			newList.append(w)
	return newList

def findLetters(c, word):
	positions = []
	for i in range(0, len(word)):
		if word[i] == c:
			positions.append(i)
	return positions

def getGuessedWord():
	guessed = []
	for i in range(0, wordSize):
		guessed.append(knownLetters[i])
		guessed.append(" ")
	return "".join(guessed)

print "EVIL HANGMAN"
wordSize = int(raw_input("Enter word size: "))
dictionary = filterLen(wordSize, list(open("dictionary.txt", 'r').read().split('\n')))

# check dictionary size
if dictionary:
	print "Invalid word size, exiting"
	exit()

# setup letter tracking
for i in range(0, wordSize):
	knownLetters[i] = '_'
for c in string.lowercase:
	guessedLetters[c] = 0

numGuessed = 0

while numGuessed < wordSize:
	# show guessed letters
	print "Secret word: " + getGuessedWord
	# get letter
	letter = raw_input("Guess a letter, if you dare: ")
	while 1:
		if (len(letter) > 1):
			letter = raw_input("That's not a letter you peasant!\nTry again: ")
		elif guessedLetters[letter] == 1:
			letter = raw_input("You already guessed that letter you fool!\nTry again: ")
		else:
			break

	# enter letter in guessedLetters
	guessedLetters[letter] = 1
	newDictionary = dictionary
	for i in range(0, wordSize):
		newDictionary = filterChar(i, letter, newDictionary)
	if newDictionary:
		# incorrect / dodged guess
		print "HA! WRONG! You will never defeat me!!\n"
		dictionary = newDictionary
		for w in dictionary:
			print(w)
	else:
		# correct guess
		print "Impossible!  Nothing more than luck...\n"
		letterPositions = findLetters(letter, dictionary[0])
		dictionary = filterWords(letterPositions, letter, dictionary)
		for i in letterPositions:
			knownLetters[i] = letter
		numGuessed += len(letterPositions)