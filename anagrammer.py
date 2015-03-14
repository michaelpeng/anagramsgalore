"""
Function to check whether two strings are anagrams of each other

Ex:
'scare'
'acres'
True
"""

def anagrammer(string1, string2):
	dict = {}
	for letter in string1:
		if letter not in dict:
			dict[letter] = 1
		else:
			dict[letter] += 1

	for letter in string2:
		if letter not in dict:
			return False
		else:
			dict[letter] -= 1

	for key, value in dict.iteritems():
		if value != 0:
			return False

	return True

string1 = raw_input("First string: ")
string2 = raw_input("Second string: ")
anagrammer(string1, string2)
