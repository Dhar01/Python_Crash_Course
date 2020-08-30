wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key, values in wardrobe.items():
	for color in values:
		print("{} {}".format(color, key))