s = input("camelCase: ")
print("snake_case: ", end="")

for c in s:
	if c.islower():
		print(c, end="")
	else:
		print("_",c.lower(), sep="", end="")
