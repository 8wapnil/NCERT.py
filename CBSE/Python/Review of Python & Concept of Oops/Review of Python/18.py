while True:
	print("For 1ˢᵗ distance...")
	x1 = (int(input("	Enter feet: ")), int(input("		Enter inches: ")))
	print("For 2ⁿᵈ distance...")
	x2 = (int(input("	Enter feet: ")), int(input("		Enter inches: ")))

	inchNet = (x1[1] + x2[1])
	inch = inchNet%12
	print(x1[0] + x2[0] + (inchNet - inch)/12, "feet, ", inch, " in")