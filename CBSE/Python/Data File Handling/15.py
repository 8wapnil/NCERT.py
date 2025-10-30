import pickle

roman = {"I": 1}

with open("roman.dat", "wb+") as rome:
	pickle.dump(roman, rome)
	rome.seek(0)
	
	try: data = pickle.load(rome)
	except EOFError: data = {}
	
	try: print(data[input("Enter roman: ")])
	except KeyError: pass