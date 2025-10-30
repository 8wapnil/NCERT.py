import pickle

with open("Story.txt") as story:
	tale = story.read().split()
	lore = story.readlines()
	with open("index.txt", "wb+") as contents:
		words = {}
		for word in tale:
			if word not in words:
				l = []
				for line in range(len(lore)):
					if word in lore[line]: l.append(line + 1)
				words[word] = l
		pickle.dump(words, contents)