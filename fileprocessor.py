print("Printing out User Data:")
f = open("fileprocessor.input", "r")
line = f.readlines()
for i in line:
	if (i.startswith("#") == False):
		i = i.split(":")
		print("The user "+i[0] +" has a password of "+i[1] +" and has userid "+ i[2] +" and groupid "+i[3])
	else:
		print("User4 is skipped because it starts with a hashtag (is commented out)")
print("End of User Data")
