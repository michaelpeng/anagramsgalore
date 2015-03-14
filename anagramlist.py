"""
Given a list of strings, tell which items are anagrams in the list, which ones are not
["scare", "sharp", "acres", "cares", "ho", "bob", "shoes", "harps", "oh"]

return list of lists, each list grouping anagrams together
"""


"""
Function to check two strings are anagrams of each other

'scare'
'acres'
True
"""
def anagrammer(string1, string2):
	this_dict = {}
	for letter in string1:
		if letter not in this_dict:
			this_dict[letter] = 1
		else:
			this_dict[letter] += 1
	for letter in string2:
		if letter not in this_dict:
			return False
		else:
			this_dict[letter] -= 1
	for key, value in this_dict.iteritems():
		if value != 0:
			return False
	return True

def anagramlist(this_list):
	anagram_dict = {}
	while len(this_list) != 0:
		item = this_list[0]
		if item not in anagram_dict:
			anagram_dict[item] = [this_list.pop(this_list.index(item))]
			for word in list(this_list):
				if anagrammer(item, word):
					anagram_dict[item].append(this_list.pop(this_list.index(word)))
		else:
			this_list.remove(item)
	return_list = []
	for key, value in anagram_dict.iteritems():
		return_list.append(value)
	print return_list


this_list = ["scare", "sharp", "acres", "cares", "ho", "bob", "shoes", "harps", "oh"]
anagramlist(this_list)