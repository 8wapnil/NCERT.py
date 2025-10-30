def replace_file(pattern_string, replacement_string, name1, name2):
	with open(name1) as f1:
		with open(name2, "w") as f2: f2.write(f1.read().replace(pattern_string, replacement_string))