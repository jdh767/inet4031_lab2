print("Printing out User Data:")
f = open("fileprocessor.input", "r")
line = f.readlines()
for i in line:
    i = i.split(":")
    print("The user "+i[0] +" has a password of "+i[1] +" and has userid "+ i[2] +" and groupid "+i[3])
print("End of User Data")
