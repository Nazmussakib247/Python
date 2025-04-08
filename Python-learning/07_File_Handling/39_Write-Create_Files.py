#Write to an existing file
f = open("Demofile.txt", "a")
f.write("Now the files has more new content!")
f.close()

#Opeing and reading file after appending
f = open("Demofile.txt", "r")
print(f.read())

#Overwrite an existing file
f = open("Demofile.txt", "w")
f.write("Opps, i've deleted file contents")
f.close()

#opening and reading after overwriting
f = open("Demofile.txt", "r")
print(f.read())

#Create a new file
#Return error if file already exists
f = open("Newfile", "x")

#create new file if doest not exist, but don't return error
f = open("Newfile", "w")