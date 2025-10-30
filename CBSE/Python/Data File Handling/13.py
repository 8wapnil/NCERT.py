def fileFunc(input_file, output_file, transformation_function):
	if transformation_function == "capitalize first alphabet of every word":
		with open(input_file) as inputFile: data = inputFile.read()
		with open(output_file) as outputFile: outputFile.write(data.capitalize())